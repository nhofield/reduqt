input_space = 'zero'

def run(qc):
    qc.initialize([(0.0009765625000000414+4.1424515142057145e-17j), (0.0009765625000001084+4.6327886115205806e-17j), (0.0009765624999999783+5.111166267437502e-17j), (0.2041015624999999+3.5069566969235524e-16j), (0.0009765625000000343+4.15441095560364e-17j), (0.0009765625000000657+3.687992741084629e-17j), (0.20410156249999997+3.707875312408666e-16j), (0.0009765625000000442+3.6999521824825547e-17j), (0.0009765625000000273+3.676033299686702e-17j), (0.0009765625000001034+3.687992741084635e-17j), (0.0009765625000000078+4.166370397001555e-17j), (0.20410156249999994+3.9578276376252646e-16j), (0.0009765625000000633+3.209615085167692e-17j), (0.0009765625000000102+2.7431968706486783e-17j), (0.0009765625000000139+3.2215745265656107e-17j), (0.0009765625000000026+3.233533967963533e-17j), (0.0009765625000000883+4.154410955603645e-17j), (0.2041015625+3.5069566969235534e-16j), (0.0009765625000000373+4.166370397001566e-17j), (0.0009765625000000247+3.69995218248255e-17j), (0.0009765624999999973+3.687992741084625e-17j), (0.0009765625000000668+3.6999521824825596e-17j), (0.20410156249999994+3.9578276376252646e-16j), (0.0009765625000000137+3.233533967963534e-17j), (0.000976562500000045+3.209615085167691e-17j), (0.0009765625000000137+3.6999521824825485e-17j), (0.0009765624999999783+3.221574526565609e-17j), (0.0009765625000000078+3.233533967963532e-17j), (0.000976562500000006+3.2215745265656144e-17j), (0.000976562500000024+2.7551563120466054e-17j), (0.0009765625000000692+3.711911623880477e-17j), (0.20410156249999994+4.658650903543574e-16j), (0.0009765625000000293+3.6760332996867055e-17j), (0.0009765625000000544+4.166370397001561e-17j), (0.000976562500000038+3.2096150851676916e-17j), (0.0009765625000000449+3.221574526565615e-17j), (0.0009765625000000436+3.113939553984307e-17j), (0.20410156249999997+3.7569090221401527e-16j), (0.0009765625000000275+3.69995218248255e-17j), (0.0009765625000000447+2.7551563120466035e-17j), (0.000976562500000052+3.209615085167692e-17j), (0.0009765625000000692+3.22157452656562e-17j), (0.0009765625000000278+2.743196870648675e-17j), (0.0009765625000000137+2.755156312046598e-17j), (0.00097656250000006+3.2215745265656144e-17j), (0.0009765625000000297+2.7551563120466008e-17j), (0.0009765625000000273+3.2335339679635346e-17j), (0.0009765625000000128+1.8103604416106524e-17j), (0.0009765625000000763+3.6879927410846313e-17j), (0.20410156249999994+4.359664868595491e-16j), (0.0009765625000000588+2.7431968706486857e-17j), (0.0009765625000000494+2.7551563120466054e-17j), (0.0009765625000000497+3.2215745265656156e-17j), (0.000976562500000024+3.233533967963537e-17j), (0.0009765624999999964+3.233533967963534e-17j), (0.0009765624999999882+2.28873809752759e-17j), (0.0009765625000000176+4.178329838399481e-17j), (0.20410156249999994+4.4086985783269763e-16j), (0.0009765624999999964+2.7551563120465998e-17j), (0.0009765624999999931+2.2887380975275906e-17j), (0.2041015625+4.609617193812089e-16j), (0.0009765625000000275+3.245493409361457e-17j), (0.20410156249999994+4.859569519028688e-16j), (0.0009765624999999894+2.3006975389255025e-17j), (0.0009765625000000518+4.1544109556036385e-17j), (0.0009765625000000351+3.209615085167692e-17j), (0.20410156249999994+3.908793927893778e-16j), (0.0009765624999999882+3.6999521824825485e-17j), (0.0009765625000000134+3.687992741084625e-17j), (0.0009765625000000729+3.221574526565622e-17j), (0.2041015625+4.35966486859549e-16j), (0.0009765624999999953+2.7551563120465974e-17j), (0.0009765625000000275+3.6879927410846246e-17j), (0.000976562500000069+2.7431968706486867e-17j), (0.20410156249999994+4.1587462531103774e-16j), (0.000976562499999998+2.6594807808632145e-17j), (0.0009765625000000596+2.7431968706486793e-17j), (0.00097656250000004+2.2767786561296728e-17j), (0.000976562499999993+3.71191162388047e-17j), (0.0009765624999999783+1.8103604416106434e-17j), (0.0009765625000000226+3.687992741084624e-17j), (0.0009765625000000275+4.1783298383994876e-17j), (0.20410156249999994+4.158746253110378e-16j), (0.0009765625000000202+2.7551563120466014e-17j), (0.0009765625000000232+3.221574526565617e-17j), (0.20410156249999994+4.207779962841863e-16j), (0.0009765625000000568+3.7119116238804743e-17j), (0.0009765624999999928+2.7671157534445115e-17j), (0.0009765624999999965+3.125898995382225e-17j), (0.000976562500000007+2.2767786561296644e-17j), (0.20410156249999994+4.609617193812088e-16j), (0.0009765624999999737+2.288738097527578e-17j), (0.0009765624999999657+2.7551563120465968e-17j), (0.0009765624999999687+2.7671157534445176e-17j), (0.0009765625000000486+2.2887380975275927e-17j), (0.0009765624999999391+1.8223198830085668e-17j), (0.0009765625000000503+3.209615085167695e-17j), (0.00097656250000003+3.2215745265656144e-17j), (0.000976562500000052+3.699952182482545e-17j), (0.0009765625000000171+2.276778656129667e-17j), (0.0009765625000000256+3.221574526565613e-17j), (0.0009765625000000373+2.7551563120466038e-17j), (0.20410156249999994+4.609617193812089e-16j), (0.0009765624999999958+2.767115753444517e-17j), (0.0009765625000000325+3.221574526565616e-17j), (0.000976562500000035+2.276778656129667e-17j), (0.0009765624999999999+3.233533967963527e-17j), (0.0009765624999999793+1.810360441610648e-17j), (0.0009765625000000245+3.2335339679635315e-17j), (0.0009765625000000102+2.288738097527593e-17j), (0.20410156249999992+4.8595695190286865e-16j), (0.0009765624999999589+1.8223198830085646e-17j), (0.000976562500000014+3.699952182482546e-17j), (0.2041015625+4.408698578326976e-16j), (0.0009765625000000243+2.7551563120465968e-17j), (0.0009765625000000054+2.7671157534445195e-17j), (0.000976562500000034+2.755156312046603e-17j), (0.0009765624999999895+3.149817878178063e-17j), (0.0009765625000000035+2.7671157534445183e-17j), (0.20410156249999994+5.109521844245287e-16j), (0.20410156249999994+4.408698578326976e-16j), (0.000976562499999998+3.723871065278391e-17j), (0.0009765624999999549+2.7671157534445053e-17j), (0.000976562499999949+1.3439422270916315e-17j), (0.2041015625+5.261406749998913e-16j), (0.2041015625+5.310440459730399e-16j), (0.0009765624999999587+2.779075194842432e-17j), (0.0009765624999999133+1.83427932440648e-17j), (0.0009765625000000416+3.676033299686706e-17j), (0.0009765625000000301+3.2096150851676935e-17j), (0.0009765625000000375+3.20961508516769e-17j), (0.0009765625000000694+3.221574526565622e-17j), (0.000976562500000022+3.209615085167695e-17j), (0.0009765625000000312+2.743196870648684e-17j), (0.0009765625+3.2215745265656045e-17j), (0.0009765625000000102+2.276778656129667e-17j), (0.0009765625000000273+3.209615085167693e-17j), (0.0009765625000000152+2.743196870648677e-17j), (0.0009765625000000275+2.743196870648677e-17j), (0.0009765625000000694+2.7551563120466085e-17j), (0.0009765625000000414+2.7431968706486826e-17j), (0.0009765625000000252+2.2767786561296678e-17j), (0.0009765625+2.2767786561296623e-17j), (0.0009765624999999979+1.8103604416106475e-17j), (0.0009765625000000434+3.2096150851676953e-17j), (0.0009765625000000416+3.221574526565617e-17j), (0.000976562500000057+2.743196870648681e-17j), (0.0009765625000000497+2.2767786561296712e-17j), (0.0009765625000000544+2.7431968706486848e-17j), (0.0009765625000000275+2.276778656129667e-17j), (0.0009765624999999861+2.7551563120465887e-17j), (0.000976562500000007+1.81036044161065e-17j), (0.0009765625000000243+2.743196870648676e-17j), (0.000976562500000007+2.27677865612966e-17j), (0.0009765624999999982+2.2767786561296533e-17j), (0.0009765624999999883+1.8103604416106475e-17j), (0.0009765625000000015+2.2767786561296638e-17j), (0.0009765624999999757+1.8103604416106505e-17j), (0.0009765624999999792+1.8103604416106487e-17j), (0.0009765624999999722+1.8223198830085696e-17j), (0.0009765625000000572+3.2096150851676935e-17j), (0.0009765625000000445+2.7431968706486774e-17j), (0.0009765625000000173+2.7431968706486786e-17j), (0.0009765625000000173+2.2767786561296644e-17j), (0.0009765625000000226+2.743196870648679e-17j), (0.0009765625+2.755156312046601e-17j), (0.0009765624999999884+2.276778656129657e-17j), (0.0009765625000000007+1.8103604416106524e-17j), (0.0009765625000000226+2.7431968706486777e-17j), (0.0009765624999999909+2.2767786561296617e-17j), (0.0009765624999999654+2.27677865612966e-17j), (0.0009765625+1.8103604416106487e-17j), (0.0009765625000000085+2.276778656129659e-17j), (0.0009765624999999957+1.810360441610645e-17j), (0.0009765624999999687+1.8103604416106413e-17j), (0.0009765624999999393+1.3439422270916262e-17j), (0.0009765625000000037+2.743196870648677e-17j), (0.0009765624999999722+2.7551563120465937e-17j), (0.0009765624999999757+2.2767786561296592e-17j), (0.0009765624999999958+1.8103604416106502e-17j), (0.000976562500000022+2.2767786561296675e-17j), (0.0009765624999999965+1.81036044161065e-17j), (0.0009765624999999896+1.810360441610645e-17j), (0.0009765624999999883+1.343942227091631e-17j), (0.0009765624999999982+2.2767786561296607e-17j), (0.0009765624999999722+2.288738097527573e-17j), (0.0009765624999999341+1.8103604416106388e-17j), (0.0009765624999999638+1.343942227091632e-17j), (0.0009765624999999584+2.288738097527578e-17j), (0.000976562499999949+1.343942227091629e-17j), (0.0009765624999999861+1.8223198830085646e-17j), (0.0009765624999999478+8.775240125726129e-18j), (0.000976562500000007+3.209615085167692e-17j), (0.0009765624999999958+2.743196870648677e-17j), (0.0009765624999999861+3.221574526565607e-17j), (0.0009765625000000278+2.2767786561296663e-17j), (0.0009765624999999914+2.743196870648673e-17j), (0.0009765625000000245+2.2767786561296663e-17j), (0.0009765624999999722+2.7551563120465813e-17j), (0.0009765625000000004+1.8103604416106527e-17j), (0.0009765625000000178+2.7431968706486734e-17j), (0.0009765625000000007+2.2767786561296617e-17j), (0.0009765624999999861+2.7551563120465912e-17j), (0.0009765624999999784+1.8103604416106465e-17j), (0.0009765624999999838+2.276778656129662e-17j), (0.0009765625000000056+1.8103604416106508e-17j), (0.0009765624999999654+1.81036044161064e-17j), (0.000976562499999954+1.343942227091629e-17j), (0.000976562500000002+2.743196870648679e-17j), (0.000976562499999949+2.27677865612966e-17j), (0.0009765624999999861+2.755156312046596e-17j), (0.0009765624999999958+1.810360441610653e-17j), (0.0009765624999999873+2.2767786561296654e-17j), (0.0009765625+2.288738097527583e-17j), (0.0009765624999999785+1.8103604416106434e-17j), (0.0009765625000000139+1.3439422270916391e-17j), (0.0009765625000000173+2.276778656129666e-17j), (0.0009765624999999863+1.8103604416106484e-17j), (0.0009765624999999722+2.288738097527573e-17j), (0.000976562499999954+1.3439422270916299e-17j), (0.0009765624999999708+1.8103604416106434e-17j), (0.0009765624999999481+1.3439422270916251e-17j), (0.0009765625+1.343942227091634e-17j), (0.0009765624999999393+8.77524012572604e-18j), (0.0009765625000000054+2.7431968706486737e-17j), (0.0009765625000000007+2.2767786561296644e-17j), (0.0009765624999999759+2.2767786561296577e-17j), (0.0009765624999999896+1.8103604416106518e-17j), (0.0009765624999999845+2.2767786561296626e-17j), (0.0009765624999999785+1.810360441610645e-17j), (0.0009765624999999861+2.288738097527583e-17j), (0.0009765624999999909+1.343942227091634e-17j), (0.0009765624999999934+2.276778656129661e-17j), (0.0009765624999999761+1.8103604416106462e-17j), (0.0009765624999999377+1.81036044161064e-17j), (0.0009765624999999378+1.3439422270916237e-17j), (0.000976562499999978+1.810360441610641e-17j), (0.0009765624999999859+1.343942227091633e-17j), (0.0009765624999999445+1.8223198830085548e-17j), (0.0009765624999999443+8.775240125726118e-18j), (0.0009765624999999935+2.27677865612966e-17j), (0.0009765624999999722+2.2887380975275804e-17j), (0.0009765624999999689+1.8103604416106382e-17j), (0.0009765624999999614+1.3439422270916294e-17j), (0.0009765624999999717+1.8103604416106438e-17j), (0.0009765624999999481+1.343942227091627e-17j), (0.0009765624999999689+1.3439422270916282e-17j), (0.0009765624999999722+1.3559016684895514e-17j), (0.0009765624999999861+2.2887380975275804e-17j), (0.0009765624999999784+1.3439422270916292e-17j), (0.0009765624999999342+1.3439422270916198e-17j), (0.0009765624999999394+8.775240125726141e-18j), (0.0009765624999999722+1.8223198830085646e-17j), (0.0009765624999999445+1.3559016684895514e-17j), (0.0009765624999999785+8.775240125726153e-18j), (0.0009765624999999274+4.111057980535953e-18j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j])
