import logging
 
from mysql.connector import MySQLConnection, Error
from NFeDBConfig import read_db_config

module_logger = logging.getLogger("NFeImport.NFeSQL")

def selectNFe(extracNFeDataResult):
  
  nfeNumber = (extracNFeDataResult[6])
  
  logger = logging.getLogger("NFeImport.NFeSQL.selectNFe")
  logger.info("SELECTING nfe %s", nfeNumber)
    
  select_stmt = """ SELECT * FROM nfe WHERE ide_nNF = %s """ 

  db_config = read_db_config()
  conn_select = MySQLConnection(**db_config)
  cursor_select = conn_select.cursor(buffered=True)

  try :
    cursor_select.execute(select_stmt, (nfeNumber,))
  except Exception as ex:
    logger.error("Exception occured: %s" % ex)

  rowCount = cursor_select.rowcount
  
  if rowCount > 0:
    deleteNFe(nfeNumber)
 
  cursor_select.close()
  conn_select.close()

def deleteNFe(nfeNumber):
  
  logger = logging.getLogger("NFeImport.NFeSQL.deleteNFe")
  logger.info("DELETING nfe %s" , nfeNumber)

  delete_nfe_stmt = """ DELETE FROM nfe  WHERE ide_nNF = %s """

  delete_nfedetalhe_stmt = """ DELETE FROM nfedetalhe WHERE nNF = %s """    

  db_config = read_db_config()
  conn_delete = MySQLConnection(**db_config)
  cursor_delete = conn_delete.cursor(buffered=True)

  try :
    cursor_delete.execute(delete_nfe_stmt, (nfeNumber,))
    cursor_delete.execute(delete_nfedetalhe_stmt, (nfeNumber,))

    conn_delete.commit()

  except Exception as ex:
    logger.error("Exception occured: %s" % ex)

  cursor_delete.close()
  conn_delete.close()

  
def insertNFe(extracNFeDataResult, extracNFeDetailResult):

  logger = logging.getLogger("NFeImport.NFeSQL.insertNFe")

  queryInsert = """INSERT INTO nfe (  ide_cUF,  ide_cNF, ide_natOp,  ide_indPag,
          ide_mod,  ide_serie, ide_nNF,  ide_dhEmi, ide_tpNF,  ide_idDest, ide_cMunFG, ide_tpImp,
          ide_tpEmis, ide_cDV, ide_tpAmb, ide_finNFe, ide_indFinal, ide_indPres, ide_procEmi, ide_verProc,
          emit_CNPJ, emit_xNome, emit_xFant, emit_xLgr, emit_nro, emit_xBairro, emit_cMun, emit_xMun,
          emit_UF, emit_CEP, emit_xPais, emit_fone, emit_IE, emit_IEST, emit_IM, emit_CNAE,
          emit_CRT, dest_CNPJ, dest_xNome, dest_xLgr, dest_nro, dest_xBairro, dest_cMun, dest_xMun,
          dest_UF, dest_CEP, dest_xPais, dest_fone, dest_indIEDest, dest_IE, total_vBC, total_vICMS,
          total_vICMSDeson, total_vFCP, total_vBCST, total_vST, total_vFCPST, total_vFCPSTRet, total_vProd, total_vFrete,
          total_vSeg, total_vDesc, total_vII, total_vIPI, total_vIPIDevol, total_vPIS, total_vCOFINS, total_vOutro,
          total_vNF, transp_modFrete, transp_CNPJ, transp_xNome, transp_IE, transp_xEnder, transp_xMun, transp_UF,
          transp_qVol, transp_marca, transp_nVol, cobr_nFat, cobr_vOrig, cobr_vDesc, cobr_vLiq, detPag_indPag,
          detPag_tPag, detPag_vPag,  infAdic_infCpl)
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

  try:
    
      db_config = read_db_config()
      conn = MySQLConnection(**db_config)

      cursor = conn.cursor()

      logger.info("INSERTING nfe")

      cursor.execute(queryInsert, (extracNFeDataResult))
      conn.commit()

      if cursor.lastrowid:

          logger.info("nfe id: %s", cursor.lastrowid)

          cursor = conn.cursor()

          for detail in extracNFeDetailResult:
              queryInsert = None
              queryInsert = """INSERT INTO nfedetalhe (  
                nNF, det_cProd, det_cEAN, det_xProd, det_NCM, det_CEST, det_CFOP, det_uCom, det_qCom, det_vUnCom, 
                det_vProd, det_cEANTrib, det_uTrib, det_qTrib, det_vUnTrib, det_indTot, det_xPed, det_ICMS_orig, 
                det_ICMS_CST, det_ICMS_modBC, det_ICMS_vBC, det_ICMS_pICMS, det_ICMS_vICMS, det_IPI_qSelo, det_IPI_cEnq, 
                det_IPI_CST, det_IPI_vBC, det_IPI_pIPI, det_IPI_vIPI, det_PIS_CST, det_PIS_vBC, det_PIS_pPIS, det_PIS_vPIS, 
                det_COFINS_CST, det_COFINS_vBC, det_COFINS_pCOFINS, det_COFINS_vCOFINS, det_infAdProd )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

              logger.info("Inserting nfedetalhe")

              cursor.execute(queryInsert, (detail))
              conn.commit()

              if cursor.lastrowid:
                logger.info("nfedetalhe id: %s", cursor.lastrowid)

      else:
          logger.error("last insert id not found")

  except Error as error:
      print(error)

  finally:
      cursor.close()
      conn.close()
