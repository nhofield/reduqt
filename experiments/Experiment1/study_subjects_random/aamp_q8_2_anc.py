input_space = 'zero'

def run(qc):
    qc.initialize([(0.014155946303051059+9.160614237471661e-17j), (0.31246661961612565+3.9642436549003235e-16j), (0.31246661961612554+3.964243654900323e-16j), (0.014155946303051009+8.763153938222952e-17j), (0.014155946303051064+7.10143162327887e-17j), (0.01415594630305102+8.01897295239557e-17j), (0.014155946303051023+7.274791966568194e-17j), (0.014155946303051038+5.959790338202777e-17j), (0.014155946303051064+7.845612609106244e-17j), (0.014155946303051066+7.274791966568201e-17j), (0.014155946303051017+7.274791966568196e-17j), (0.01415594630305099+6.70397132403015e-17j), (0.014155946303051071+6.530610980740826e-17j), (0.01415594630305104+5.959790338202776e-17j), (0.014155946303051026+5.959790338202776e-17j), (0.01415594630305099+6.1331506814921e-17j), (0.014155946303051085+7.845612609106249e-17j), (0.014155946303051097+8.018972952395582e-17j), (0.014155946303051076+7.274791966568205e-17j), (0.01415594630305103+5.283262169268801e-17j), (0.014155946303051049+6.530610980740823e-17j), (0.014155946303051083+5.959790338202781e-17j), (0.014155946303051038+6.703971324030158e-17j), (0.014155946303051012+5.3889696956647287e-17j), (0.31246661961612554+4.637812013095216e-16j), (0.01415594630305101+6.70397132403015e-17j), (0.014155946303051037+6.703971324030154e-17j), (0.01415594630305098+6.1331506814921e-17j), (0.014155946303051035+6.703971324030156e-17j), (0.014155946303050984+5.3889696956647256e-17j), (0.014155946303050998+5.3889696956647274e-17j), (0.01415594630305096+4.8181490531266694e-17j), (0.014155946303051002+7.101431623278864e-17j), (0.01415594630305102+9.507334924050326e-17j), (0.01415594630305094+8.018972952395568e-17j), (0.31246661961612565+5.60228748393172e-16j), (0.014155946303050983+7.274791966568191e-17j), (0.31246661961612565+5.311380371290109e-16j), (0.01415594630305101+6.703971324030152e-17j), (0.014155946303050993+7.62151265314686e-17j), (0.014155946303051024+6.530610980740823e-17j), (0.014155946303051043+6.703971324030152e-17j), (0.014155946303051037+6.703971324030152e-17j), (0.3124666196161257+6.857670067409836e-16j), (0.014155946303051049+5.95979033820278e-17j), (0.01415594630305099+6.877331667319479e-17j), (0.014155946303050965+6.133150681492101e-17j), (0.31246661961612565+6.949424200321508e-16j), (0.014155946303051017+7.274791966568197e-17j), (0.3124666196161257+5.311380371290111e-16j), (0.014155946303051024+6.703971324030149e-17j), (0.014155946303051002+7.621512653146865e-17j), (0.014155946303051009+6.703971324030152e-17j), (0.014155946303050991+6.877331667319474e-17j), (0.31246661961612565+5.984948729485005e-16j), (0.01415594630305098+5.562330038954049e-17j), (0.01415594630305099+6.703971324030149e-17j), (0.014155946303050986+6.877331667319477e-17j), (0.014155946303050981+6.1331506814921e-17j), (0.31246661961612576+6.949424200321508e-16j), (0.014155946303050984+5.388969695664721e-17j), (0.014155946303050941+4.818149053126665e-17j), (0.014155946303050967+5.562330038954047e-17j), (0.014155946303050976+5.735690382243382e-17j), (0.014155946303051016+7.101431623278863e-17j), (0.014155946303051004+7.274791966568196e-17j), (0.014155946303051031+7.274791966568194e-17j), (0.01415594630305101+5.959790338202774e-17j), (0.01415594630305102+6.530610980740822e-17j), (0.014155946303051+5.959790338202771e-17j), (0.014155946303050969+5.95979033820277e-17j), (0.014155946303050997+5.3889696956647287e-17j), (0.01415594630305101+6.53061098074082e-17j), (0.014155946303051012+5.959790338202773e-17j), (0.014155946303051017+5.959790338202777e-17j), (0.01415594630305097+5.388969695664728e-17j), (0.014155946303051017+5.959790338202777e-17j), (0.014155946303050969+5.3889696956647274e-17j), (0.01415594630305098+5.388969695664722e-17j), (0.014155946303050991+4.8181490531266774e-17j), (0.014155946303051033+6.530610980740822e-17j), (0.01415594630305104+5.95979033820277e-17j), (0.014155946303051023+5.959790338202773e-17j), (0.01415594630305099+5.3889696956647256e-17j), (0.014155946303051002+5.959790338202776e-17j), (0.01415594630305096+5.3889696956647244e-17j), (0.014155946303051021+5.388969695664729e-17j), (0.014155946303050969+4.818149053126675e-17j), (0.014155946303051031+6.703971324030156e-17j), (0.01415594630305097+5.3889696956647256e-17j), (0.014155946303050983+5.388969695664728e-17j), (0.014155946303050981+4.8181490531266774e-17j), (0.014155946303050995+5.388969695664729e-17j), (0.01415594630305101+4.8181490531266774e-17j), (0.014155946303050962+4.8181490531266725e-17j), (0.014155946303050948+4.24732841058862e-17j), (0.014155946303051028+6.530610980740823e-17j), (0.014155946303051021+5.959790338202776e-17j), (0.014155946303051021+5.959790338202777e-17j), (0.014155946303051004+6.133150681492107e-17j), (0.014155946303051026+5.95979033820278e-17j), (0.014155946303050976+6.133150681492097e-17j), (0.014155946303050984+5.3889696956647274e-17j), (0.014155946303050991+4.818149053126681e-17j), (0.014155946303051026+5.959790338202779e-17j), (0.014155946303050991+5.388969695664726e-17j), (0.014155946303050993+5.3889696956647256e-17j), (0.014155946303050976+5.562330038954055e-17j), (0.014155946303051002+5.388969695664732e-17j), (0.014155946303050995+4.818149053126678e-17j), (0.014155946303050957+4.818149053126676e-17j), (0.014155946303050976+4.9915093964160083e-17j), (0.014155946303051017+5.959790338202775e-17j), (0.014155946303050976+6.133150681492102e-17j), (0.014155946303051+5.388969695664722e-17j), (0.014155946303050964+4.818149053126678e-17j), (0.014155946303051026+5.388969695664734e-17j), (0.01415594630305098+4.818149053126673e-17j), (0.014155946303050976+5.56233003895405e-17j), (0.014155946303050957+4.2473284105886244e-17j), (0.01415594630305105+5.3889696956647274e-17j), (0.01415594630305099+4.818149053126674e-17j), (0.01415594630305097+4.8181490531266756e-17j), (0.014155946303050948+4.9915093964159837e-17j), (0.014155946303051007+4.8181490531266805e-17j), (0.014155946303050967+4.2473284105886274e-17j), (0.01415594630305095+4.247328410588624e-17j), (0.014155946303050936+3.676507768050568e-17j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j])
