input_space = 'zero'

def run(qc):
    qc.initialize([(-0.015624999999999934+1.758037885494751e-17j), (-0.015624999999999936+8.012825736608795e-18j), (-0.015624999999999927+1.5666868231279748e-17j), (0.17187499999999992+3.263731557493286e-16j), (-0.015624999999999941+1.5666868231279742e-17j), (-0.015624999999999941+9.926336360276521e-18j), (0.17187499999999992+3.072380495126513e-16j), (0.1718749999999999+3.4742177260967376e-16j), (-0.015624999999999903+8.012825736608812e-18j), (-0.01562499999999992-1.5547273817298824e-18j), (-0.015624999999999944+6.099315112941055e-18j), (-0.015624999999999944+3.5878324193782004e-19j), (-0.015624999999999905+2.2722938656056272e-18j), (-0.015624999999999946-3.4682380053976395e-18j), (-0.015624999999999964+4.185804489273304e-18j), (-0.015624999999999964-9.208769876400918e-18j), (0.17187499999999992+2.670543264156287e-16j), (-0.015624999999999941+9.926336360276538e-18j), (-0.015624999999999918+2.1407400102282968e-17j), (0.17187499999999994+3.4742177260967386e-16j), (0.17187499999999994+3.4550826198600613e-16j), (0.17187499999999994+3.2828666637299645e-16j), (0.17187499999999994+3.4742177260967386e-16j), (-0.015624999999999993+2.2722938656054912e-18j), (0.17187499999999992+3.2637315574932866e-16j), (-0.01562499999999994-3.4682380053976788e-18j), (0.17187499999999997+3.282866663729965e-16j), (-0.015624999999999977-1.5547273817299636e-18j), (0.17187499999999994+3.856919850830286e-16j), (-0.01562499999999998-5.3817486290654725e-18j), (-0.015624999999999948+2.2722938656056037e-18j), (-0.015624999999999974-1.8776322994739703e-17j), (-0.015624999999999908+3.58783241937802e-19j), (-0.015624999999999922+6.0993151129410386e-18j), (-0.015624999999999938+6.099315112941009e-18j), (0.17187499999999994+3.282866663729965e-16j), (0.17187499999999992+2.8810294327597393e-16j), (0.171875+3.4742177260967396e-16j), (-0.015624999999999964+8.012825736608769e-18j), (-0.015624999999999946-1.5547273817299945e-18j), (-0.015624999999999946-1.5547273817298797e-18j), (-0.015624999999999913-3.4682380053975956e-18j), (-0.015624999999999929-3.4682380053976464e-18j), (-0.015624999999999977-5.381748629065412e-18j), (-0.015624999999999969+1.1839846983944226e-17j), (0.17187499999999994+3.6847038947001897e-16j), (0.17187499999999997+3.493352832333417e-16j), (-0.015624999999999995-1.1122280500068689e-17j), (-0.015624999999999951+6.0993151129410324e-18j), (-0.01562499999999996-7.295259252733186e-18j), (0.17187499999999997+3.091515601363191e-16j), (-0.015624999999999998+2.2722938656053926e-18j), (-0.015624999999999938+4.185804489273292e-18j), (-0.015624999999999953-5.381748629065398e-18j), (-0.015624999999999953-1.5547273817299498e-18j), (-0.015624999999999995-1.8776322994739663e-17j), (-0.015624999999999938+4.185804489273259e-18j), (-0.015624999999999967-9.208769876400927e-18j), (-0.015624999999999983-1.5547273817299914e-18j), (0.171875+3.8951900633036427e-16j), (0.1718749999999999+3.6847038947001897e-16j), (-0.015625000000000014-1.1122280500068787e-17j), (-0.015625000000000003-1.1122280500068738e-17j), (-0.015625000000000028-2.0689833618407526e-17j), (0.17187499999999992+2.479192201789513e-16j), (-0.01562499999999995+2.2722938656055587e-18j), (0.17187499999999997+3.2637315574932876e-16j), (-0.015624999999999953+8.012825736608805e-18j), (-0.015624999999999934+2.2722938656055775e-18j), (-0.015624999999999964-7.295259252733157e-18j), (-0.015624999999999988+8.012825736608743e-18j), (-0.015624999999999964-9.208769876400918e-18j), (-0.01562499999999997+6.099315112940985e-18j), (-0.015624999999999957-3.4682380053976734e-18j), (0.17187499999999994+3.665568788463512e-16j), (0.171875+3.68470389470019e-16j), (-0.015624999999999967-3.4682380053976965e-18j), (-0.015625000000000017-1.303579112373643e-17j), (0.171875+3.8760549570669633e-16j), (-0.015624999999999969-1.1122280500068681e-17j), (-0.015624999999999918+9.926336360276506e-18j), (-0.015624999999999972-3.4682380053976595e-18j), (0.17187499999999994+3.4742177260967376e-16j), (0.1718749999999999+3.8760549570669633e-16j), (-0.015624999999999943+3.5878324193782235e-19j), (-0.015625000000000007-9.208769876400974e-18j), (-0.015624999999999964-5.3817486290654856e-18j), (-0.015624999999999984-1.494930174740424e-17j), (-0.015624999999999944+4.1858044892732695e-18j), (-0.015624999999999991-1.3035791123736432e-17j), (-0.015624999999999998+2.2722938656054897e-18j), (-0.01562500000000002-1.1122280500068729e-17j), (0.17187499999999994+3.8760549570669633e-16j), (-0.015624999999999986-2.2603344242075133e-17j), (0.17187499999999994+4.277892188037189e-16j), (-0.015625000000000007-2.0689833618407437e-17j), (-0.015624999999999941+2.2722938656055344e-18j), (-0.015624999999999958-7.29525925273316e-18j), (-0.015624999999999962+3.587832419377738e-19j), (-0.015625000000000003-9.208769876400964e-18j), (-0.015624999999999977+4.1858044892732e-18j), (-0.015624999999999977-9.208769876400955e-18j), (0.171875+3.6847038947001906e-16j), (-0.015624999999999997-1.4949301747404196e-17j), (-0.015624999999999993+3.5878324193772836e-19j), (-0.015624999999999981-1.3035791123736407e-17j), (-0.015625000000000028-9.208769876401017e-18j), (-0.015625000000000014-1.4949301747404255e-17j), (0.171875+3.4933528323334165e-16j), (-0.015624999999999993-1.1122280500068667e-17j), (-0.015624999999999984-3.4682380053977897e-18j), (-0.015625000000000028-2.4516854865743006e-17j), (-0.015624999999999981-3.468238005397728e-18j), (-0.01562500000000001-1.3035791123736476e-17j), (-0.01562500000000002-1.5547273817300515e-18j), (-0.015625000000000045-1.4949301747404347e-17j), (-0.015624999999999965-9.208769876400915e-18j), (-0.015625000000000066-1.8776322994739793e-17j), (0.171875+4.0865411256704173e-16j), (-0.015625000000000066-2.0689833618407545e-17j), (0.17187499999999994+3.493352832333416e-16j), (-0.015624999999999993-2.260334424207515e-17j), (-0.015625-1.4949301747404285e-17j), (-0.01562500000000004-2.0689833618407517e-17j), (-0.01562500000000001-3.4682380053977912e-18j), (-0.01562500000000008-2.4516854865743027e-17j), (-0.015624999999999983-1.6862812371071926e-17j), (-0.01562500000000005-3.02573867367463e-17j), (-0.015624999999999915+4.185804489273331e-18j), (-0.015624999999999929-1.5547273817298897e-18j), (-0.015624999999999951-1.554727381729936e-18j), (-0.015624999999999944-3.468238005397674e-18j), (-0.015624999999999894-1.5547273817298227e-18j), (-0.015624999999999943-7.295259252733117e-18j), (-0.015624999999999944-3.468238005397625e-18j), (-0.015624999999999972-9.208769876400909e-18j), (-0.015624999999999962-1.5547273817299105e-18j), (-0.015624999999999953-7.295259252733137e-18j), (-0.015624999999999984-7.295259252733154e-18j), (-0.015624999999999984-1.3035791123736422e-17j), (-0.01562499999999995-7.295259252733141e-18j), (-0.015624999999999962-1.3035791123736382e-17j), (-0.015624999999999965-1.3035791123736438e-17j), (-0.015624999999999955-1.87763229947396e-17j), (-0.015624999999999944+2.27229386560561e-18j), (-0.015624999999999953-7.295259252733127e-18j), (-0.015624999999999981-7.295259252733192e-18j), (-0.015625000000000014-9.208769876401032e-18j), (-0.01562499999999993-3.4682380053975755e-18j), (-0.015624999999999972-9.208769876400884e-18j), (-0.015624999999999958-9.208769876400909e-18j), (-0.01562500000000001-1.8776322994739694e-17j), (-0.015625-3.468238005397674e-18j), (-0.015624999999999984-1.3035791123736379e-17j), (-0.015625-9.208769876401007e-18j), (-0.015625-1.8776322994739734e-17j), (-0.015624999999999986-9.208769876400958e-18j), (-0.01562500000000001-1.8776322994739725e-17j), (-0.015625000000000028-1.8776322994739753e-17j), (-0.01562500000000002-2.4516854865742978e-17j), (-0.015624999999999946-1.5547273817299107e-18j), (-0.015624999999999957-7.295259252733129e-18j), (-0.015624999999999995-7.295259252733206e-18j), (-0.015625000000000014-9.208769876400983e-18j), (-0.015624999999999944-3.468238005397625e-18j), (-0.01562499999999993-9.208769876400909e-18j), (-0.015625000000000003-1.3035791123736445e-17j), (-0.01562500000000001-1.877632299473971e-17j), (-0.015624999999999962-7.295259252733198e-18j), (-0.01562499999999997-1.3035791123736428e-17j), (-0.015625-1.3035791123736472e-17j), (-0.015624999999999995-1.8776322994739648e-17j), (-0.01562500000000001-1.3035791123736456e-17j), (-0.015625000000000028-1.4949301747404242e-17j), (-0.015625000000000014-1.494930174740429e-17j), (-0.01562500000000002-2.4516854865742987e-17j), (-0.015624999999999948-7.295259252733157e-18j), (-0.015625000000000003-1.3035791123736442e-17j), (-0.015625000000000014-9.208769876401007e-18j), (-0.015624999999999974-1.8776322994739712e-17j), (-0.015624999999999967-1.3035791123736388e-17j), (-0.015625000000000024-1.877632299473976e-17j), (-0.015625000000000014-1.8776322994739734e-17j), (-0.01562500000000004-2.4516854865742978e-17j), (-0.01562500000000002-1.303579112373649e-17j), (-0.015625000000000003-1.8776322994739694e-17j), (-0.01562500000000004-1.877632299473977e-17j), (-0.015625000000000028-2.0689833618407502e-17j), (-0.015625000000000014-1.494930174740412e-17j), (-0.015625000000000045-2.4516854865743027e-17j), (-0.015625000000000003-2.451685486574293e-17j), (-0.015625000000000045-3.025738673674626e-17j), (-0.015624999999999944+2.2722938656055113e-18j), (-0.01562499999999998-7.29525925273318e-18j), (-0.015625-3.4682380053977728e-18j), (-0.015624999999999995-1.3035791123736442e-17j), (-0.015624999999999944-7.295259252733152e-18j), (-0.015624999999999965-1.303579112373643e-17j), (-0.01562499999999997-1.3035791123736413e-17j), (-0.015625000000000003-1.8776322994739663e-17j), (-0.015624999999999958-7.295259252733215e-18j), (-0.015624999999999962-1.3035791123736407e-17j), (-0.015624999999999986-9.208769876400983e-18j), (-0.015625000000000014-1.4949301747404218e-17j), (-0.01562499999999997-1.3035791123736396e-17j), (-0.015624999999999965-1.8776322994739645e-17j), (-0.015625000000000014-1.4949301747404242e-17j), (-0.015624999999999995-2.4516854865742923e-17j), (-0.015624999999999981-7.295259252733185e-18j), (-0.015624999999999965-1.3035791123736398e-17j), (-0.015624999999999972-9.208769876400909e-18j), (-0.015625000000000028-1.494930174740434e-17j), (-0.015624999999999946-1.3035791123736345e-17j), (-0.01562499999999999-1.8776322994739645e-17j), (-0.015625000000000003-1.87763229947397e-17j), (-0.015625000000000014-2.4516854865742923e-17j), (-0.015624999999999984-1.3035791123736475e-17j), (-0.015624999999999986-1.8776322994739657e-17j), (-0.01562499999999998-1.877632299473965e-17j), (-0.01562499999999999-2.451685486574292e-17j), (-0.015624999999999986-1.4949301747404144e-17j), (-0.015625000000000017-2.4516854865742972e-17j), (-0.015624999999999986-2.0689833618407403e-17j), (-0.015625000000000024-3.0257386736746216e-17j), (-0.015624999999999977-7.295259252733158e-18j), (-0.015624999999999955-1.3035791123736379e-17j), (-0.015625000000000007-1.3035791123736496e-17j), (-0.015625000000000003-1.877632299473971e-17j), (-0.015624999999999941-1.3035791123736364e-17j), (-0.015625-1.8776322994739666e-17j), (-0.015624999999999986-1.4949301747404144e-17j), (-0.015625000000000007-2.451685486574294e-17j), (-0.015625000000000017-1.3035791123736444e-17j), (-0.015624999999999986-1.8776322994739666e-17j), (-0.015625000000000014-1.8776322994739697e-17j), (-0.01562500000000004-2.451685486574303e-17j), (-0.015625000000000014-1.4949301747404218e-17j), (-0.015624999999999974-2.451685486574298e-17j), (-0.015625000000000024-2.4516854865742975e-17j), (-0.015625000000000028-3.025738673674622e-17j), (-0.015624999999999991-1.3035791123736453e-17j), (-0.015625000000000007-1.87763229947397e-17j), (-0.015625000000000024-1.877632299473973e-17j), (-0.01562500000000002-2.4516854865743024e-17j), (-0.015624999999999983-1.877632299473968e-17j), (-0.015625000000000024-2.4516854865743033e-17j), (-0.01562500000000007-2.0689833618407502e-17j), (-0.015625000000000062-3.025738673674632e-17j), (-0.015624999999999986-1.4949301747404218e-17j), (-0.01562500000000003-2.4516854865742972e-17j), (-0.015625000000000003-2.4516854865742944e-17j), (-0.015625000000000045-3.025738673674627e-17j), (-0.015625000000000035-2.451685486574294e-17j), (-0.015625000000000035-3.02573867367463e-17j), (-0.015625000000000038-3.025738673674628e-17j), (-0.015625000000000056-3.599791860774957e-17j), 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j, 0j])
