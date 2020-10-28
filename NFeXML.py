import os
import xml.dom.minidom as minidom


"""
Dados da NFe
"""
def extractNFeData(xml):
    doc = minidom.parse(xml)
    node = doc.documentElement
    nfeData = []

    # 
    # Identificação da NFe
    #     
    ides = doc.getElementsByTagName("ide")
    for ide in ides:
        nfeData.append(ide.getElementsByTagName("cUF")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("cNF")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("natOp")[0].childNodes[0].nodeValue)

        # opcional
        hasElement = ide.getElementsByTagName("indPag")
        if len(hasElement) != 0:
          nfeData.append(ide.getElementsByTagName("indPag")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("indPag")
        #
            
        nfeData.append(ide.getElementsByTagName("mod")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("serie")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("nNF")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("dhEmi")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("tpNF")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("idDest")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("cMunFG")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("tpImp")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("tpEmis")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("cDV")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("tpAmb")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("finNFe")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("indFinal")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("indPres")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("procEmi")[0].childNodes[0].nodeValue)
        nfeData.append(ide.getElementsByTagName("verProc")[0].childNodes[0].nodeValue)

    # 
    # Emitente
    #         
    emits = doc.getElementsByTagName("emit")
    for emit in emits:
        nfeData.append(emit.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xNome")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xFant")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xLgr")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("nro")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xBairro")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("cMun")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xMun")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("UF")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("CEP")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("xPais")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("fone")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("IE")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("IEST")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("IM")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("CNAE")[0].childNodes[0].nodeValue)
        nfeData.append(emit.getElementsByTagName("CRT")[0].childNodes[0].nodeValue)

    # 
    # Destinatário
    #         
    dests = doc.getElementsByTagName("dest")
    for dest in dests:
        nfeData.append(dest.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("xNome")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("xLgr")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("nro")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("xBairro")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("cMun")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("xMun")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("UF")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("CEP")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("xPais")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("fone")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("indIEDest")[0].childNodes[0].nodeValue)
        nfeData.append(dest.getElementsByTagName("IE")[0].childNodes[0].nodeValue)

    # 
    # Totais e Impostos
    #         
    totals = doc.getElementsByTagName("total")
    for total in totals:
        nfeData.append(total.getElementsByTagName("vBC")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vICMS")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vICMSDeson")[0].childNodes[0].nodeValue)
        
        # opcional
        hasElement = total.getElementsByTagName("vFCP")
        if len(hasElement) != 0:
          nfeData.append(total.getElementsByTagName("vFCP")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..vFCP..")
        #        
        
        nfeData.append(total.getElementsByTagName("vBCST")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vST")[0].childNodes[0].nodeValue)

        hasElement = total.getElementsByTagName("vFCPST")
        if len(hasElement) != 0:
          nfeData.append(total.getElementsByTagName("vFCPST")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..vFCPST..")
        #        
        hasElement = total.getElementsByTagName("vFCPSTRet")
        if len(hasElement) != 0:
          nfeData.append(total.getElementsByTagName("vFCPSTRet")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..vFCPSTRet..")
        #
        
        nfeData.append(total.getElementsByTagName("vProd")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vFrete")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vSeg")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vDesc")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vII")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vIPI")[0].childNodes[0].nodeValue)
        
        #        
        hasElement = total.getElementsByTagName("vIPIDevol")
        if len(hasElement) != 0:
          nfeData.append(total.getElementsByTagName("vIPIDevol")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..vIPIDevol..")
        #
        
        nfeData.append(total.getElementsByTagName("vPIS")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vCOFINS")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vOutro")[0].childNodes[0].nodeValue)
        nfeData.append(total.getElementsByTagName("vNF")[0].childNodes[0].nodeValue)

    # 
    # Transportadora
    #         
    transps = doc.getElementsByTagName("transp")
    for transp in transps:
        nfeData.append(transp.getElementsByTagName("modFrete")[0].childNodes[0].nodeValue)
        
        # opcional
        hasElement = transp.getElementsByTagName("CNPJ")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("CNPJ")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..CNPJ..")
        #
        hasElement = transp.getElementsByTagName("xNome")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("xNome")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..xNome..")
        #
        hasElement = transp.getElementsByTagName("IE")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("IE")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..IE..")
        #              
        hasElement = transp.getElementsByTagName("xEnder")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("xEnder")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..xEnder..")
        # 
        hasElement = transp.getElementsByTagName("xMun")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("xMun")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..xMun..")
        # 
        hasElement = transp.getElementsByTagName("UF")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("UF")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..UF..")
        # 
        hasElement = transp.getElementsByTagName("qVol")
        if len(hasElement) != 0:
          nfeData.append(transp.getElementsByTagName("qVol")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..qVol..")
        #
        
        nfeData.append(transp.getElementsByTagName("marca")[0].childNodes[0].nodeValue)
        nfeData.append(transp.getElementsByTagName("nVol")[0].childNodes[0].nodeValue)

    # 
    # Cobrança
    # 
    cobrs = doc.getElementsByTagName("fat")
    
    for cobr in cobrs:      
      nfeData.append(cobr.getElementsByTagName("nFat")[0].childNodes[0].nodeValue)
      nfeData.append(cobr.getElementsByTagName("vOrig")[0].childNodes[0].nodeValue)

      hasElement = cobr.getElementsByTagName("vDesc")
      if len(hasElement) != 0:
        nfeData.append(cobr.getElementsByTagName("vDesc")[0].childNodes[0].nodeValue)
      else:
        nfeData.append("..vDesc..")
      #

      nfeData.append(cobr.getElementsByTagName("vLiq")[0].childNodes[0].nodeValue)

    # 
    # Pagamento
    # 
    
    '''
    No layout antigo Pagamento nao vinha
    '''
    if len(doc.getElementsByTagName("pag")) != 0:

      pags = doc.getElementsByTagName("pag")

      for pag in pags:    
        # 
        hasElement = pag.getElementsByTagName("indPag")
        if len(hasElement) != 0:
          nfeData.append(pag.getElementsByTagName("indPag")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..indPag..")
        #    
        hasElement = pag.getElementsByTagName("tPag")
        if len(hasElement) != 0:
          nfeData.append(pag.getElementsByTagName("tPag")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..tPag..")
        # 
        hasElement = pag.getElementsByTagName("vPag")
        if len(hasElement) != 0:
          nfeData.append(pag.getElementsByTagName("vPag")[0].childNodes[0].nodeValue)
        else:
          nfeData.append("..vPag..")
    else:
      nfeData.append("..indPag..")
      nfeData.append("..tPag..")
      nfeData.append("..vPag..")      

    # 
    # Informação Adicional
    #       
    infAdics = doc.getElementsByTagName("infAdic")
    
    for infAdic in infAdics: 
      nfeData.append(infAdic.getElementsByTagName("infCpl")[0].childNodes[0].nodeValue)

    return nfeData

"""
Produtos da NFe (Detalhes)
"""
def extractNFeDetail(xml):
    doc = minidom.parse(xml)
    node = doc.documentElement
    nfeDetalhe = []
    nfeDetalhes = []
    nfeNumero = None

    ides = doc.getElementsByTagName("ide")
    for ide in ides:
        nfeNumero = ide.getElementsByTagName("nNF")[0].childNodes[0].nodeValue

    dets = doc.getElementsByTagName("det")
    for det in dets:

        #
        # Produtos
        #
        prods = det.getElementsByTagName("prod")
        for prod in prods:
            nfeDetalhe.append(nfeNumero)
            nfeDetalhe.append(prod.getElementsByTagName("cProd")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("cEAN")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("xProd")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("NCM")[0].childNodes[0].nodeValue)
            
            # opcional
            hasElement = prod.getElementsByTagName("CEST")
            if len(hasElement) != 0:
              nfeDetalhe.append(prod.getElementsByTagName("CEST")[0].childNodes[0].nodeValue)
            else:
              nfeDetalhe.append("..CEST..")
            #
            
            nfeDetalhe.append(prod.getElementsByTagName("CFOP")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("uCom")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("qCom")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("vUnCom")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("vProd")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("cEANTrib")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("uTrib")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("qTrib")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("vUnTrib")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("indTot")[0].childNodes[0].nodeValue)
            nfeDetalhe.append(prod.getElementsByTagName("xPed")[0].childNodes[0].nodeValue)

        #
        # Imposto ICMS
        #
        impostos = det.getElementsByTagName("imposto")
        for imposto in impostos:
            icmss = det.getElementsByTagName("ICMS")
            for icms in icmss:
                nfeDetalhe.append(icms.getElementsByTagName("orig")[0].childNodes[0].nodeValue)
                nfeDetalhe.append(icms.getElementsByTagName("CST")[0].childNodes[0].nodeValue)
                
                hasElement = icms.getElementsByTagName("modBC")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("modBC")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("modBC")
                # 
                hasElement = icms.getElementsByTagName("vBC")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("vBC")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("..vBC..")
                #
                hasElement = icms.getElementsByTagName("pICMS")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("pICMS")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("..pICMS..")
                #
                hasElement = icms.getElementsByTagName("vICMS")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("vICMS")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("..vICMS..")
                #
                # <28-10-2020>
                #
                hasElement = icms.getElementsByTagName("modBCST")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("modBCST")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("0")
                #
                hasElement = icms.getElementsByTagName("pMVAST")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("pMVAST")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("0.00")
                #
                hasElement = icms.getElementsByTagName("vBCST")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("vBCST")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("0.00")
                #
                hasElement = icms.getElementsByTagName("pICMSST")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("pICMSST")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("0.00")
                #
                hasElement = icms.getElementsByTagName("vICMSST")
                if len(hasElement) != 0:
                  nfeDetalhe.append(icms.getElementsByTagName("vICMSST")[0].childNodes[0].nodeValue)
                else:
                  nfeDetalhe.append("0.00")
                #
                # </28-10-2020>

        #
        # IPI
        #
        impostos = det.getElementsByTagName("imposto")
        for imposto in impostos:
            ipis = det.getElementsByTagName("IPI")
            for ipi in ipis:
              hasElement = ipi.getElementsByTagName("qSelo")
              if len(hasElement) != 0:
                nfeDetalhe.append(ipi.getElementsByTagName("qSelo")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..qSelo..")
              #             
              nfeDetalhe.append(ipi.getElementsByTagName("cEnq")[0].childNodes[0].nodeValue)
              nfeDetalhe.append(ipi.getElementsByTagName("CST")[0].childNodes[0].nodeValue)

              #
              hasElement = ipi.getElementsByTagName("vBC")
              if len(hasElement) != 0:
                nfeDetalhe.append(ipi.getElementsByTagName("vBC")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..vBC..")
              #
              hasElement = ipi.getElementsByTagName("pIPI")
              if len(hasElement) != 0:
                nfeDetalhe.append(ipi.getElementsByTagName("pIPI")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..pIPI..")
              #
              hasElement = ipi.getElementsByTagName("vIPI")
              if len(hasElement) != 0:
                nfeDetalhe.append(ipi.getElementsByTagName("vIPI")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..vIPI..")
              #

        #
        # PIS
        #
        impostos = det.getElementsByTagName("imposto")
        for imposto in impostos:
            piss = det.getElementsByTagName("PIS")
            for pis in piss:
              nfeDetalhe.append(pis.getElementsByTagName("CST")[0].childNodes[0].nodeValue)
              
              #
              hasElement = pis.getElementsByTagName("vBC")
              if len(hasElement) != 0:
                nfeDetalhe.append(pis.getElementsByTagName("vBC")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..vBC..")
              #
              hasElement = pis.getElementsByTagName("pPIS")
              if len(hasElement) != 0:
                nfeDetalhe.append(pis.getElementsByTagName("pPIS")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..pPIS..")
              #
              hasElement = pis.getElementsByTagName("vPIS")
              if len(hasElement) != 0:
                nfeDetalhe.append(pis.getElementsByTagName("vPIS")[0].childNodes[0].nodeValue)
              else:
                nfeDetalhe.append("..vPIS..")
                
        #
        # COFINS
        #
        impostos = det.getElementsByTagName("imposto")
        for imposto in impostos:
          cofinss = det.getElementsByTagName("COFINS")
          for cofins in cofinss:
            nfeDetalhe.append(cofins.getElementsByTagName("CST")[0].childNodes[0].nodeValue)
            #
            hasElement = cofins.getElementsByTagName("vBC")
            if len(hasElement) != 0:
              nfeDetalhe.append(cofins.getElementsByTagName("vBC")[0].childNodes[0].nodeValue)
            else:
              nfeDetalhe.append("0.00")
            #
            hasElement = cofins.getElementsByTagName("pCOFINS")
            if len(hasElement) != 0:
              nfeDetalhe.append(cofins.getElementsByTagName("pCOFINS")[0].childNodes[0].nodeValue)
            else:
              nfeDetalhe.append("0.00")
            #
            hasElement = cofins.getElementsByTagName("vCOFINS")
            if len(hasElement) != 0:
              nfeDetalhe.append(cofins.getElementsByTagName("vCOFINS")[0].childNodes[0].nodeValue)
            else:
              nfeDetalhe.append("0.00")
              
        #
        # Informação Adicional do Produto
        #
        hasElement = det.getElementsByTagName("infAdProd")
        if len(hasElement) != 0:
          nfeDetalhe.append(det.getElementsByTagName("infAdProd")[0].childNodes[0].nodeValue)
        else:
          nfeDetalhe.append("0.00")

        nfeDetalhes.append(nfeDetalhe)
        nfeDetalhe = []

    return nfeDetalhes
