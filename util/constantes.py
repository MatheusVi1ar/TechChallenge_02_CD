url = "https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br"
access_key = ''
secret_key = ''
session_token = ''

html_text = """<form novalidate="" class="ng-untouched ng-pristine ng-valid">
   <h2>Carteira do Dia - 26/12/24</h2>
   <p>Carteira Teórica do IBovespa válida para&nbsp;26/12/24</p>
   <div class="row">
      <div class="col-12 col-md-4">
         <div class="form-group">
            <label for="exampleFormControlSelect1">Consulta por</label>
            <select id="segment" formcontrolname="segment" class="form-control ng-untouched ng-pristine ng-valid">
               <option value="1">Código</option>
               <option value="2">Setor de Atuação</option>
            </select>
         </div>
      </div>
      <div class="col-md-4 col-12">
         <div class="form-group"><label for="exampleFormControlSelect1"></label><input type="text" id="keyword" formcontrolname="keyword" maxlength="30" class="form-control ng-untouched ng-pristine ng-valid" placeholder="Código ou ação"></div>
      </div>
      <div class="form-group col-md-2 col-12 form-inline"><label for="botao"></label><button type="submit" class="btn btn-primary btn-xs-block mt-3">BUSCAR</button></div>
      <div class="form-group col-md-2 col-12 form-inline"><label for="botao"></label><button type="butto" class="btn btn-primary btn-xs-block mt-3">LIMPAR</button></div>
   </div>
   <div class="row">
      <div class="col-12">
         <p>Esta tabela considera as variações na participação de cada um dos papéis na composição total do índice, apuradas para a abertura do dia.</p>
         <table class="table table-responsive-sm table-responsive-md">
            <thead>
               <tr>
                  <th>Código</th>
                  <th>Ação</th>
                  <th>Tipo</th>
                  <th>Qtde. Teórica</th>
                  <th>Part. (%)</th>
               </tr>
            </thead>
            <tbody>
               <tr>
                  <td>ALOS3</td>
                  <td>ALLOS</td>
                  <td>ON  EJ  NM</td>
                  <td class="text-right">502.481.592</td>
                  <td class="text-right">0,473</td>
               </tr>
               <tr>
                  <td>ALPA4</td>
                  <td>ALPARGATAS</td>
                  <td>PN      N1</td>
                  <td class="text-right">166.460.180</td>
                  <td class="text-right">0,053</td>
               </tr>
               <tr>
                  <td>ABEV3</td>
                  <td>AMBEV S/A</td>
                  <td>ON  EDJ</td>
                  <td class="text-right">4.394.835.131</td>
                  <td class="text-right">2,747</td>
               </tr>
               <tr>
                  <td>ASAI3</td>
                  <td>ASSAI</td>
                  <td>ON      NM</td>
                  <td class="text-right">1.349.687.675</td>
                  <td class="text-right">0,400</td>
               </tr>
               <tr>
                  <td>AURE3</td>
                  <td>AUREN</td>
                  <td>ON      NM</td>
                  <td class="text-right">291.727.616</td>
                  <td class="text-right">0,131</td>
               </tr>
               <tr>
                  <td>AMOB3</td>
                  <td>AUTOMOB</td>
                  <td>ON      NM</td>
                  <td class="text-right">558.603.452</td>
                  <td class="text-right">0,010</td>
               </tr>
               <tr>
                  <td>AZUL4</td>
                  <td>AZUL</td>
                  <td>PN      N2</td>
                  <td class="text-right">328.421.113</td>
                  <td class="text-right">0,055</td>
               </tr>
               <tr>
                  <td>AZZA3</td>
                  <td>AZZAS 2154</td>
                  <td>ON      NM</td>
                  <td class="text-right">127.330.493</td>
                  <td class="text-right">0,191</td>
               </tr>
               <tr>
                  <td>B3SA3</td>
                  <td>B3</td>
                  <td>ON      NM</td>
                  <td class="text-right">5.511.401.013</td>
                  <td class="text-right">2,893</td>
               </tr>
               <tr>
                  <td>BBSE3</td>
                  <td>BBSEGURIDADE</td>
                  <td>ON      NM</td>
                  <td class="text-right">637.332.335</td>
                  <td class="text-right">1,190</td>
               </tr>
               <tr>
                  <td>BBDC3</td>
                  <td>BRADESCO</td>
                  <td>ON      N1</td>
                  <td class="text-right">1.484.426.957</td>
                  <td class="text-right">0,806</td>
               </tr>
               <tr>
                  <td>BBDC4</td>
                  <td>BRADESCO</td>
                  <td>PN      N1</td>
                  <td class="text-right">5.129.958.973</td>
                  <td class="text-right">3,031</td>
               </tr>
               <tr>
                  <td>BRAP4</td>
                  <td>BRADESPAR</td>
                  <td>PN  EJ  N1</td>
                  <td class="text-right">250.969.312</td>
                  <td class="text-right">0,215</td>
               </tr>
               <tr>
                  <td>BBAS3</td>
                  <td>BRASIL</td>
                  <td>ON      NM</td>
                  <td class="text-right">2.842.613.858</td>
                  <td class="text-right">3,478</td>
               </tr>
               <tr>
                  <td>BRKM5</td>
                  <td>BRASKEM</td>
                  <td>PNA     N1</td>
                  <td class="text-right">265.388.400</td>
                  <td class="text-right">0,160</td>
               </tr>
               <tr>
                  <td>BRAV3</td>
                  <td>BRAVA</td>
                  <td>ON      NM</td>
                  <td class="text-right">463.981.130</td>
                  <td class="text-right">0,454</td>
               </tr>
               <tr>
                  <td>BRFS3</td>
                  <td>BRF SA</td>
                  <td>ON  EJ  NM</td>
                  <td class="text-right">814.523.002</td>
                  <td class="text-right">1,085</td>
               </tr>
               <tr>
                  <td>BPAC11</td>
                  <td>BTGP BANCO</td>
                  <td>UNT EX  N2</td>
                  <td class="text-right">1.287.247.964</td>
                  <td class="text-right">1,839</td>
               </tr>
               <tr>
                  <td>CXSE3</td>
                  <td>CAIXA SEGURI</td>
                  <td>ON      NM</td>
                  <td class="text-right">517.500.000</td>
                  <td class="text-right">0,395</td>
               </tr>
               <tr>
                  <td>CRFB3</td>
                  <td>CARREFOUR BR</td>
                  <td>ON  EJ  NM</td>
                  <td class="text-right">531.901.983</td>
                  <td class="text-right">0,153</td>
               </tr>
               <!---->
            </tbody>
            <tfoot>
               <tr>
                  <td colspan="3"> Quantidade Teórica Total </td>
                  <td class="text-right">97.041.528.920</td>
                  <td class="text-right">100,000</td>
               </tr>
               <tr>
                  <td colspan="3"> Redutor </td>
                  <td class="text-right">16.186.814,49198993</td>
                  <td></td>
               </tr>
            </tfoot>
            <!---->
         </table>
         <div class="row">
            <div class="col-md-6">
               <div class="row">
                  <div class="col-md-3 col-sm-4 col-4 mb-2">
                     <select id="selectPage" formcontrolname="selectPage" class="form-control ng-untouched ng-pristine ng-valid">
                        <option>20</option>
                        <option>40</option>
                        <option>60</option>
                        <option>120</option>
                     </select>
                  </div>
                  <div class="col-md-6 col-sm-8 col-8"><label class="pt-2">Resultados por página</label></div>
               </div>
            </div>
            <div class="col-md-6">
               <nav aria-label="Navegação de página exemplo" class="right">
                  <pagination-controls id="listing_pagination" directionlinks="true" previouslabel="" nextlabel="">
                     <pagination-template>
                        <ul class="ngx-pagination" aria-label="Pagination">
                           <li class="pagination-previous disabled">
                              <!----><span>  <span class="show-for-sr">page</span></span><!---->
                           </li>
                           <!---->
                           <li class="small-screen"> 1 / 5 </li>
                           <li class="current">
                              <!----><span class="show-for-sr">You're on page </span><span>1</span><!----><!---->
                           </li>
                           <li>
                              <a tabindex="0"><span class="show-for-sr">page </span><span>2</span></a><!----><!---->
                           </li>
                           <li>
                              <a tabindex="0"><span class="show-for-sr">page </span><span>3</span></a><!----><!---->
                           </li>
                           <li>
                              <a tabindex="0"><span class="show-for-sr">page </span><span>4</span></a><!----><!---->
                           </li>
                           <li>
                              <a tabindex="0"><span class="show-for-sr">page </span><span>5</span></a><!----><!---->
                           </li>
                           <!---->
                           <li class="pagination-next">
                              <a tabindex="0" aria-label=" page">  <span class="show-for-sr">page</span></a><!----><!---->
                           </li>
                           <!---->
                        </ul>
                        <!---->
                     </pagination-template>
                  </pagination-controls>
               </nav>
            </div>
         </div>
         <!---->
         <div class="row mt-3">
            <div class="col-md-12">
               <div class="list-avatar">
                  <div class="list-avatar-row">
                     <div class="primary-action"><img src="assets/img/ic_cloud_download_black_48dp.png" alt=""></div>
                     <div class="content">
                        <p class="primary-text"><a href="/indexPage/day/IBOV?language=pt-br">Download</a></p>
                     </div>
                  </div>
                  <div class="divider"></div>
               </div>
            </div>
         </div>
      </div>
   </div>
   <!----><!----><!---->
</form>"""