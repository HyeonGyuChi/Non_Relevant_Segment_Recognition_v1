"""
    patients information file (fold)
"""
# 117ea중 116 ea (04_GS4_99_L_47 제거)
gangbuk_samsung_patients = ['04_GS4_99_L_1', '04_GS4_99_L_2', '04_GS4_99_L_3', '04_GS4_99_L_4', '04_GS4_99_L_5', '04_GS4_99_L_6', '04_GS4_99_L_7', '04_GS4_99_L_8', '04_GS4_99_L_9', '04_GS4_99_L_10', '04_GS4_99_L_11',
                        '04_GS4_99_L_12', '04_GS4_99_L_13', '04_GS4_99_L_14', '04_GS4_99_L_16', '04_GS4_99_L_17', '04_GS4_99_L_18', '04_GS4_99_L_19', '04_GS4_99_L_20', '04_GS4_99_L_21', '04_GS4_99_L_22', '04_GS4_99_L_25',
                        '04_GS4_99_L_26', '04_GS4_99_L_27', '04_GS4_99_L_28', '04_GS4_99_L_29', '04_GS4_99_L_30', '04_GS4_99_L_32', '04_GS4_99_L_34', '04_GS4_99_L_36', '04_GS4_99_L_37', '04_GS4_99_L_38', '04_GS4_99_L_39',
                        '04_GS4_99_L_40', '04_GS4_99_L_41', '04_GS4_99_L_42', '04_GS4_99_L_43', '04_GS4_99_L_44', '04_GS4_99_L_45', '04_GS4_99_L_46', '04_GS4_99_L_48', '04_GS4_99_L_49', '04_GS4_99_L_50', '04_GS4_99_L_51',
                        '04_GS4_99_L_52', '04_GS4_99_L_53', '04_GS4_99_L_55', '04_GS4_99_L_56', '04_GS4_99_L_57', '04_GS4_99_L_58', '04_GS4_99_L_59', '04_GS4_99_L_60', '04_GS4_99_L_61', '04_GS4_99_L_62', '04_GS4_99_L_63',
                        '04_GS4_99_L_64', '04_GS4_99_L_65', '04_GS4_99_L_66', '04_GS4_99_L_67', '04_GS4_99_L_68', '04_GS4_99_L_69', '04_GS4_99_L_70', '04_GS4_99_L_71', '04_GS4_99_L_72', '04_GS4_99_L_73', '04_GS4_99_L_74',
                        '04_GS4_99_L_75', '04_GS4_99_L_76', '04_GS4_99_L_77', '04_GS4_99_L_79', '04_GS4_99_L_80', '04_GS4_99_L_81', '04_GS4_99_L_82', '04_GS4_99_L_83', '04_GS4_99_L_84', '04_GS4_99_L_85', '04_GS4_99_L_86',
                        '04_GS4_99_L_87', '04_GS4_99_L_88', '04_GS4_99_L_89', '04_GS4_99_L_90', '04_GS4_99_L_91', '04_GS4_99_L_92', '04_GS4_99_L_94', '04_GS4_99_L_95', '04_GS4_99_L_96', '04_GS4_99_L_97', '04_GS4_99_L_98',
                        '04_GS4_99_L_99', '04_GS4_99_L_100', '04_GS4_99_L_101', '04_GS4_99_L_102', '04_GS4_99_L_103', '04_GS4_99_L_104', '04_GS4_99_L_105', '04_GS4_99_L_106', '04_GS4_99_L_107', '04_GS4_99_L_108', '04_GS4_99_L_109',
                        '04_GS4_99_L_110', '04_GS4_99_L_111', '04_GS4_99_L_112', '04_GS4_99_L_113', '04_GS4_99_L_114', '04_GS4_99_L_115', '04_GS4_99_L_116', '04_GS4_99_L_117', '04_GS4_99_L_118', '04_GS4_99_L_120', '04_GS4_99_L_121',
                        '04_GS4_99_L_122', '04_GS4_99_L_123', '04_GS4_99_L_124', '04_GS4_99_L_125', '04_GS4_99_L_126', '04_GS4_99_L_127']

# 총 161ea (04_GS4_99_L_47_01, 02, 03 제거)
# ['04_GS4_99_L_79_02', '04_GS4_99_L_118_02'] ==> 해당 케이스는 01로 시작하지 않는 케이스 (161개는 해당 케이스도 포함된 개수)
# i.e, 04_GS4_99_L_79 의 경우 annotation 02,03만 존재, video는 01,02,03 존재 ?
# i.e, 04_GS4_99_L_118_02 의 경우 annotation 02만 존재, video는 01,02 존재 ?
gangbuk_samsung_videos = ['04_GS4_99_L_1_01', '04_GS4_99_L_1_02', '04_GS4_99_L_2_01', '04_GS4_99_L_3_01', '04_GS4_99_L_4_01', '04_GS4_99_L_4_02', '04_GS4_99_L_4_03', '04_GS4_99_L_4_04',
                        '04_GS4_99_L_5_01', '04_GS4_99_L_5_02', '04_GS4_99_L_6_01', '04_GS4_99_L_7_01', '04_GS4_99_L_8_01', '04_GS4_99_L_9_01', '04_GS4_99_L_10_01', '04_GS4_99_L_11_01', '04_GS4_99_L_12_01',
                        '04_GS4_99_L_13_01', '04_GS4_99_L_14_01', '04_GS4_99_L_16_01', '04_GS4_99_L_17_01', '04_GS4_99_L_17_02', '04_GS4_99_L_18_01', '04_GS4_99_L_19_01', '04_GS4_99_L_20_01', '04_GS4_99_L_20_02',
                        '04_GS4_99_L_21_01', '04_GS4_99_L_21_02', '04_GS4_99_L_21_03', '04_GS4_99_L_22_01', '04_GS4_99_L_22_02', '04_GS4_99_L_25_01', '04_GS4_99_L_26_01', '04_GS4_99_L_26_02', '04_GS4_99_L_27_01',
                        '04_GS4_99_L_28_01', '04_GS4_99_L_29_01', '04_GS4_99_L_30_01', '04_GS4_99_L_30_02', '04_GS4_99_L_32_01', '04_GS4_99_L_34_01', '04_GS4_99_L_36_01', '04_GS4_99_L_37_01', '04_GS4_99_L_38_01',
                        '04_GS4_99_L_39_01', '04_GS4_99_L_40_01', '04_GS4_99_L_40_02', '04_GS4_99_L_41_01', '04_GS4_99_L_42_01', '04_GS4_99_L_43_01', '04_GS4_99_L_44_01', '04_GS4_99_L_45_01', '04_GS4_99_L_46_01',
                        '04_GS4_99_L_48_01', '04_GS4_99_L_49_01', '04_GS4_99_L_49_02', '04_GS4_99_L_49_03', '04_GS4_99_L_49_04', '04_GS4_99_L_50_01', '04_GS4_99_L_51_01', '04_GS4_99_L_51_02', '04_GS4_99_L_51_03',
                        '04_GS4_99_L_52_01', '04_GS4_99_L_52_02', '04_GS4_99_L_53_01', '04_GS4_99_L_55_01', '04_GS4_99_L_55_02', '04_GS4_99_L_55_03', '04_GS4_99_L_56_01', '04_GS4_99_L_56_02', '04_GS4_99_L_57_01',
                        '04_GS4_99_L_58_01', '04_GS4_99_L_58_02', '04_GS4_99_L_58_03', '04_GS4_99_L_59_01', '04_GS4_99_L_60_01', '04_GS4_99_L_60_02', '04_GS4_99_L_61_01', '04_GS4_99_L_61_02', '04_GS4_99_L_61_03',
                        '04_GS4_99_L_62_01', '04_GS4_99_L_63_01', '04_GS4_99_L_64_01', '04_GS4_99_L_65_01', '04_GS4_99_L_65_02', '04_GS4_99_L_65_03', '04_GS4_99_L_65_04', '04_GS4_99_L_65_05', '04_GS4_99_L_66_01',
                        '04_GS4_99_L_67_01', '04_GS4_99_L_67_02', '04_GS4_99_L_67_03', '04_GS4_99_L_68_01', '04_GS4_99_L_69_01', '04_GS4_99_L_70_01', '04_GS4_99_L_70_02', '04_GS4_99_L_70_03', '04_GS4_99_L_71_01',
                        '04_GS4_99_L_72_01', '04_GS4_99_L_73_01', '04_GS4_99_L_74_01', '04_GS4_99_L_74_02', '04_GS4_99_L_74_03', '04_GS4_99_L_75_01', '04_GS4_99_L_76_01', '04_GS4_99_L_77_01', '04_GS4_99_L_77_02',
                        '04_GS4_99_L_79_02', '04_GS4_99_L_79_03', '04_GS4_99_L_80_01', '04_GS4_99_L_81_01', '04_GS4_99_L_81_02', '04_GS4_99_L_82_01', '04_GS4_99_L_83_01', '04_GS4_99_L_83_02', '04_GS4_99_L_83_03',
                        '04_GS4_99_L_84_01', '04_GS4_99_L_85_01', '04_GS4_99_L_86_01', '04_GS4_99_L_87_01', '04_GS4_99_L_88_01', '04_GS4_99_L_89_01', '04_GS4_99_L_90_01', '04_GS4_99_L_91_01', '04_GS4_99_L_92_01',
                        '04_GS4_99_L_94_01', '04_GS4_99_L_95_01', '04_GS4_99_L_96_01', '04_GS4_99_L_96_02', '04_GS4_99_L_96_03', '04_GS4_99_L_96_04', '04_GS4_99_L_97_01', '04_GS4_99_L_98_01', '04_GS4_99_L_99_01',
                        '04_GS4_99_L_100_01', '04_GS4_99_L_101_01', '04_GS4_99_L_102_01', '04_GS4_99_L_103_01', '04_GS4_99_L_104_01', '04_GS4_99_L_105_01', '04_GS4_99_L_106_01', '04_GS4_99_L_107_01',
                        '04_GS4_99_L_108_01', '04_GS4_99_L_109_01', '04_GS4_99_L_110_01', '04_GS4_99_L_111_01', '04_GS4_99_L_112_01', '04_GS4_99_L_113_01', '04_GS4_99_L_114_01', '04_GS4_99_L_115_01',
                        '04_GS4_99_L_116_01', '04_GS4_99_L_117_01', '04_GS4_99_L_118_02', '04_GS4_99_L_120_01', '04_GS4_99_L_121_01', '04_GS4_99_L_122_01', '04_GS4_99_L_123_01', '04_GS4_99_L_124_01',
                        '04_GS4_99_L_125_01', '04_GS4_99_L_126_01', '04_GS4_99_L_127_01']


# 42ea
severance_1st_patients =  ['01_VIHUB1.2_A9_L_2', '01_VIHUB1.2_A9_L_3', '01_VIHUB1.2_A9_L_4', '01_VIHUB1.2_A9_L_5', '01_VIHUB1.2_A9_L_6', '01_VIHUB1.2_B4_L_1', '01_VIHUB1.2_B4_L_2', '01_VIHUB1.2_B4_L_3',
                        '01_VIHUB1.2_B4_L_4', '01_VIHUB1.2_B4_L_5', '01_VIHUB1.2_B4_L_6', '01_VIHUB1.2_B4_L_7', '01_VIHUB1.2_B4_L_8', '01_VIHUB1.2_B4_L_9', '01_VIHUB1.2_B4_L_10', '01_VIHUB1.2_B4_L_11', '01_VIHUB1.2_B4_L_12',
                        '01_VIHUB1.2_B4_L_13', '01_VIHUB1.2_B4_L_14', '01_VIHUB1.2_B4_L_15', '01_VIHUB1.2_B4_L_16', '01_VIHUB1.2_B4_L_17', '01_VIHUB1.2_B4_L_18', '01_VIHUB1.2_B4_L_19', '01_VIHUB1.2_B4_L_20', '01_VIHUB1.2_B4_L_21',
                        '01_VIHUB1.2_B4_L_22', '01_VIHUB1.2_B4_L_23', '01_VIHUB1.2_B4_L_24', '01_VIHUB1.2_B4_L_25', '01_VIHUB1.2_B4_L_26', '01_VIHUB1.2_B4_L_27', '01_VIHUB1.2_B4_L_28', '01_VIHUB1.2_B4_L_29', '01_VIHUB1.2_B4_L_30',
                        '01_VIHUB1.2_B4_L_31', '01_VIHUB1.2_B4_L_33', '01_VIHUB1.2_B4_L_34', '01_VIHUB1.2_B4_L_35', '01_VIHUB1.2_B4_L_36', '01_VIHUB1.2_B4_L_37', '01_VIHUB1.2_B5_L_9']

# 92ea
severance_1st_videos =  ['01_VIHUB1.2_A9_L_2_01', '01_VIHUB1.2_A9_L_2_02', '01_VIHUB1.2_A9_L_3_01', '01_VIHUB1.2_A9_L_3_02', '01_VIHUB1.2_A9_L_3_03', '01_VIHUB1.2_A9_L_4_01', '01_VIHUB1.2_A9_L_4_02', '01_VIHUB1.2_A9_L_4_03',
                        '01_VIHUB1.2_A9_L_5_01', '01_VIHUB1.2_A9_L_5_02', '01_VIHUB1.2_A9_L_6_01', '01_VIHUB1.2_A9_L_6_02', '01_VIHUB1.2_A9_L_6_03', '01_VIHUB1.2_B4_L_1_01', '01_VIHUB1.2_B4_L_1_02', '01_VIHUB1.2_B4_L_1_03', '01_VIHUB1.2_B4_L_1_04',
                        '01_VIHUB1.2_B4_L_2_01', '01_VIHUB1.2_B4_L_2_02', '01_VIHUB1.2_B4_L_3_01', '01_VIHUB1.2_B4_L_3_02', '01_VIHUB1.2_B4_L_3_03', '01_VIHUB1.2_B4_L_4_01', '01_VIHUB1.2_B4_L_4_02', '01_VIHUB1.2_B4_L_4_03', '01_VIHUB1.2_B4_L_4_04',
                        '01_VIHUB1.2_B4_L_5_01', '01_VIHUB1.2_B4_L_6_01', '01_VIHUB1.2_B4_L_6_02', '01_VIHUB1.2_B4_L_7_01', '01_VIHUB1.2_B4_L_7_02', '01_VIHUB1.2_B4_L_8_01', '01_VIHUB1.2_B4_L_8_02', '01_VIHUB1.2_B4_L_9_01', '01_VIHUB1.2_B4_L_9_02', '01_VIHUB1.2_B4_L_9_03',
                        '01_VIHUB1.2_B4_L_10_01', '01_VIHUB1.2_B4_L_10_02', '01_VIHUB1.2_B4_L_11_01', '01_VIHUB1.2_B4_L_11_02', '01_VIHUB1.2_B4_L_11_03', '01_VIHUB1.2_B4_L_11_04', '01_VIHUB1.2_B4_L_12_01', '01_VIHUB1.2_B4_L_12_02',
                        '01_VIHUB1.2_B4_L_13_01', '01_VIHUB1.2_B4_L_13_02', '01_VIHUB1.2_B4_L_13_03', '01_VIHUB1.2_B4_L_14_01', '01_VIHUB1.2_B4_L_15_01', '01_VIHUB1.2_B4_L_15_02', '01_VIHUB1.2_B4_L_15_03', '01_VIHUB1.2_B4_L_16_01',
                        '01_VIHUB1.2_B4_L_17_01', '01_VIHUB1.2_B4_L_17_02', '01_VIHUB1.2_B4_L_18_01', '01_VIHUB1.2_B4_L_18_02', '01_VIHUB1.2_B4_L_18_03', '01_VIHUB1.2_B4_L_19_01', '01_VIHUB1.2_B4_L_19_02', '01_VIHUB1.2_B4_L_19_03',
                        '01_VIHUB1.2_B4_L_20_01', '01_VIHUB1.2_B4_L_20_02', '01_VIHUB1.2_B4_L_21_01', '01_VIHUB1.2_B4_L_21_02', '01_VIHUB1.2_B4_L_21_03', '01_VIHUB1.2_B4_L_22_01', '01_VIHUB1.2_B4_L_23_01', '01_VIHUB1.2_B4_L_24_01',
                        '01_VIHUB1.2_B4_L_25_01', '01_VIHUB1.2_B4_L_25_02', '01_VIHUB1.2_B4_L_26_01', '01_VIHUB1.2_B4_L_26_02', '01_VIHUB1.2_B4_L_27_01', '01_VIHUB1.2_B4_L_27_02', '01_VIHUB1.2_B4_L_27_03', '01_VIHUB1.2_B4_L_28_01',
                        '01_VIHUB1.2_B4_L_29_01', '01_VIHUB1.2_B4_L_30_01', '01_VIHUB1.2_B4_L_30_02', '01_VIHUB1.2_B4_L_31_01', '01_VIHUB1.2_B4_L_31_02', '01_VIHUB1.2_B4_L_33_01', '01_VIHUB1.2_B4_L_34_01',
                        '01_VIHUB1.2_B4_L_35_01', '01_VIHUB1.2_B4_L_35_02', '01_VIHUB1.2_B4_L_35_03', '01_VIHUB1.2_B4_L_36_01', '01_VIHUB1.2_B4_L_36_02', '01_VIHUB1.2_B4_L_36_03', '01_VIHUB1.2_B4_L_36_04',
                        '01_VIHUB1.2_B4_L_37_01', '01_VIHUB1.2_B5_L_9_01']

# 117ea중 115ea (01_VIHUB1.2_A9_L_33, 01_VIHUB1.2_B4_L_79 제거)
severance_2nd_patients = ['01_VIHUB1.2_A9_L_13', '01_VIHUB1.2_A9_L_14', '01_VIHUB1.2_A9_L_15', '01_VIHUB1.2_A9_L_16', '01_VIHUB1.2_A9_L_18', '01_VIHUB1.2_A9_L_19', '01_VIHUB1.2_A9_L_20', '01_VIHUB1.2_A9_L_21', '01_VIHUB1.2_A9_L_22', '01_VIHUB1.2_A9_L_23',
                        '01_VIHUB1.2_A9_L_24', '01_VIHUB1.2_A9_L_25', '01_VIHUB1.2_A9_L_26', '01_VIHUB1.2_A9_L_27', '01_VIHUB1.2_A9_L_29', '01_VIHUB1.2_A9_L_30', '01_VIHUB1.2_A9_L_31', '01_VIHUB1.2_A9_L_32', '01_VIHUB1.2_A9_L_34', '01_VIHUB1.2_A9_L_35',
                        '01_VIHUB1.2_A9_L_36', '01_VIHUB1.2_A9_L_37', '01_VIHUB1.2_A9_L_38', '01_VIHUB1.2_A9_L_39', '01_VIHUB1.2_A9_L_40', '01_VIHUB1.2_A9_L_41', '01_VIHUB1.2_A9_L_42', '01_VIHUB1.2_A9_L_43', '01_VIHUB1.2_A9_L_44', '01_VIHUB1.2_A9_L_46', '01_VIHUB1.2_A9_L_47',
                        '01_VIHUB1.2_A9_L_48', '01_VIHUB1.2_A9_L_49', '01_VIHUB1.2_A9_L_50', '01_VIHUB1.2_A9_L_51', '01_VIHUB1.2_A9_L_52', '01_VIHUB1.2_A9_L_53', '01_VIHUB1.2_B4_L_75', '01_VIHUB1.2_B4_L_76', '01_VIHUB1.2_B4_L_77', '01_VIHUB1.2_B4_L_80', '01_VIHUB1.2_B4_L_81',
                        '01_VIHUB1.2_B4_L_82', '01_VIHUB1.2_B4_L_83', '01_VIHUB1.2_B4_L_84', '01_VIHUB1.2_B4_L_85', '01_VIHUB1.2_B4_L_86', '01_VIHUB1.2_B4_L_87', '01_VIHUB1.2_B4_L_88', '01_VIHUB1.2_B4_L_89', '01_VIHUB1.2_B4_L_90', '01_VIHUB1.2_B4_L_91', '01_VIHUB1.2_B4_L_92',
                        '01_VIHUB1.2_B4_L_93', '01_VIHUB1.2_B4_L_94', '01_VIHUB1.2_B4_L_95', '01_VIHUB1.2_B4_L_96', '01_VIHUB1.2_B4_L_98', '01_VIHUB1.2_B4_L_99', '01_VIHUB1.2_B4_L_100', '01_VIHUB1.2_B4_L_101', '01_VIHUB1.2_B4_L_102', '01_VIHUB1.2_B4_L_103', '01_VIHUB1.2_B4_L_104',
                        '01_VIHUB1.2_B4_L_105', '01_VIHUB1.2_B4_L_106', '01_VIHUB1.2_B4_L_107', '01_VIHUB1.2_B4_L_108', '01_VIHUB1.2_B4_L_109', '01_VIHUB1.2_B4_L_110', '01_VIHUB1.2_B4_L_111', '01_VIHUB1.2_B4_L_112', '01_VIHUB1.2_B4_L_113', '01_VIHUB1.2_B4_L_114', '01_VIHUB1.2_B4_L_115',
                        '01_VIHUB1.2_B4_L_116', '01_VIHUB1.2_B4_L_117', '01_VIHUB1.2_B4_L_118', '01_VIHUB1.2_B4_L_119', '01_VIHUB1.2_B4_L_120', '01_VIHUB1.2_B4_L_121', '01_VIHUB1.2_B4_L_122', '01_VIHUB1.2_B4_L_123', '01_VIHUB1.2_B4_L_124', '01_VIHUB1.2_B4_L_125', '01_VIHUB1.2_B4_L_126',
                        '01_VIHUB1.2_B4_L_127', '01_VIHUB1.2_B4_L_128', '01_VIHUB1.2_B4_L_129', '01_VIHUB1.2_B4_L_130', '01_VIHUB1.2_B4_L_131', '01_VIHUB1.2_B4_L_132', '01_VIHUB1.2_B4_L_133', '01_VIHUB1.2_B4_L_134', '01_VIHUB1.2_B4_L_135', '01_VIHUB1.2_B4_L_136', '01_VIHUB1.2_B4_L_137',
                        '01_VIHUB1.2_B4_L_138', '01_VIHUB1.2_B4_L_139', '01_VIHUB1.2_B4_L_140', '01_VIHUB1.2_B4_L_141', '01_VIHUB1.2_B4_L_142', '01_VIHUB1.2_B4_L_143', '01_VIHUB1.2_B4_L_144', '01_VIHUB1.2_B4_L_145', '01_VIHUB1.2_B4_L_146', '01_VIHUB1.2_B4_L_147', '01_VIHUB1.2_B4_L_148',
                        '01_VIHUB1.2_B4_L_149', '01_VIHUB1.2_B4_L_150', '01_VIHUB1.2_B4_L_151', '01_VIHUB1.2_B4_L_152', '01_VIHUB1.2_B4_L_153', '01_VIHUB1.2_B4_L_154', '01_VIHUB1.2_B4_L_155']

# 총 284ea
# 01_VIHUB1.2_A9_L_33 01,02,03 제거
# 01_VIHUB1.2_B4_L_79 01,02,03,04,05 제거
severance_2nd_videos =  ['01_VIHUB1.2_A9_L_13_01', '01_VIHUB1.2_A9_L_13_02', '01_VIHUB1.2_A9_L_13_03', '01_VIHUB1.2_A9_L_14_01', '01_VIHUB1.2_A9_L_14_02', '01_VIHUB1.2_A9_L_14_03', '01_VIHUB1.2_A9_L_15_01', '01_VIHUB1.2_A9_L_16_01', '01_VIHUB1.2_A9_L_16_02', '01_VIHUB1.2_A9_L_16_03',
                        '01_VIHUB1.2_A9_L_18_01', '01_VIHUB1.2_A9_L_18_02', '01_VIHUB1.2_A9_L_19_01', '01_VIHUB1.2_A9_L_19_02', '01_VIHUB1.2_A9_L_19_03', '01_VIHUB1.2_A9_L_20_01', '01_VIHUB1.2_A9_L_20_02', '01_VIHUB1.2_A9_L_20_03', '01_VIHUB1.2_A9_L_21_01', '01_VIHUB1.2_A9_L_21_02',
                        '01_VIHUB1.2_A9_L_22_01', '01_VIHUB1.2_A9_L_22_02', '01_VIHUB1.2_A9_L_22_03', '01_VIHUB1.2_A9_L_23_01', '01_VIHUB1.2_A9_L_23_02', '01_VIHUB1.2_A9_L_23_03', '01_VIHUB1.2_A9_L_24_01', '01_VIHUB1.2_A9_L_24_02', '01_VIHUB1.2_A9_L_25_01', '01_VIHUB1.2_A9_L_25_02',
                        '01_VIHUB1.2_A9_L_26_01', '01_VIHUB1.2_A9_L_27_01', '01_VIHUB1.2_A9_L_29_01', '01_VIHUB1.2_A9_L_29_02', '01_VIHUB1.2_A9_L_30_01', '01_VIHUB1.2_A9_L_30_02', '01_VIHUB1.2_A9_L_31_01', '01_VIHUB1.2_A9_L_31_02', '01_VIHUB1.2_A9_L_31_03',
                        '01_VIHUB1.2_A9_L_32_01', '01_VIHUB1.2_A9_L_32_02', '01_VIHUB1.2_A9_L_32_03', '01_VIHUB1.2_A9_L_34_01', '01_VIHUB1.2_A9_L_34_02', '01_VIHUB1.2_A9_L_35_01', '01_VIHUB1.2_A9_L_35_02', '01_VIHUB1.2_A9_L_36_01', '01_VIHUB1.2_A9_L_36_02',
                        '01_VIHUB1.2_A9_L_37_01', '01_VIHUB1.2_A9_L_37_02', '01_VIHUB1.2_A9_L_37_03', '01_VIHUB1.2_A9_L_38_01', '01_VIHUB1.2_A9_L_38_02', '01_VIHUB1.2_A9_L_38_03', '01_VIHUB1.2_A9_L_39_01', '01_VIHUB1.2_A9_L_39_02', '01_VIHUB1.2_A9_L_39_03',
                        '01_VIHUB1.2_A9_L_40_01', '01_VIHUB1.2_A9_L_40_02', '01_VIHUB1.2_A9_L_40_03', '01_VIHUB1.2_A9_L_40_04', '01_VIHUB1.2_A9_L_40_05', '01_VIHUB1.2_A9_L_41_01', '01_VIHUB1.2_A9_L_42_01', '01_VIHUB1.2_A9_L_42_02', '01_VIHUB1.2_A9_L_43_01',
                        '01_VIHUB1.2_A9_L_43_02', '01_VIHUB1.2_A9_L_44_01', '01_VIHUB1.2_A9_L_44_02', '01_VIHUB1.2_A9_L_44_03', '01_VIHUB1.2_A9_L_44_04', '01_VIHUB1.2_A9_L_46_01', '01_VIHUB1.2_A9_L_46_02',
                        '01_VIHUB1.2_A9_L_47_01', '01_VIHUB1.2_A9_L_47_02', '01_VIHUB1.2_A9_L_47_03', '01_VIHUB1.2_A9_L_47_04', '01_VIHUB1.2_A9_L_48_01', '01_VIHUB1.2_A9_L_48_02', '01_VIHUB1.2_A9_L_48_03', '01_VIHUB1.2_A9_L_49_01', '01_VIHUB1.2_A9_L_49_02', '01_VIHUB1.2_A9_L_49_03',
                        '01_VIHUB1.2_A9_L_50_01', '01_VIHUB1.2_A9_L_50_02', '01_VIHUB1.2_A9_L_51_01', '01_VIHUB1.2_A9_L_51_02', '01_VIHUB1.2_A9_L_51_03', '01_VIHUB1.2_A9_L_52_01', '01_VIHUB1.2_A9_L_52_02', '01_VIHUB1.2_A9_L_52_03', '01_VIHUB1.2_A9_L_53_01', '01_VIHUB1.2_A9_L_53_02', '01_VIHUB1.2_A9_L_53_03',
                        '01_VIHUB1.2_B4_L_75_01', '01_VIHUB1.2_B4_L_75_02', '01_VIHUB1.2_B4_L_75_03', '01_VIHUB1.2_B4_L_76_01', '01_VIHUB1.2_B4_L_77_01', '01_VIHUB1.2_B4_L_77_02', '01_VIHUB1.2_B4_L_80_01', '01_VIHUB1.2_B4_L_80_02', '01_VIHUB1.2_B4_L_80_03', '01_VIHUB1.2_B4_L_80_04',
                        '01_VIHUB1.2_B4_L_81_01', '01_VIHUB1.2_B4_L_81_02', '01_VIHUB1.2_B4_L_82_01', '01_VIHUB1.2_B4_L_83_01', '01_VIHUB1.2_B4_L_83_02', '01_VIHUB1.2_B4_L_83_03', '01_VIHUB1.2_B4_L_84_01', '01_VIHUB1.2_B4_L_84_02', '01_VIHUB1.2_B4_L_85_01', '01_VIHUB1.2_B4_L_86_01',
                        '01_VIHUB1.2_B4_L_87_01', '01_VIHUB1.2_B4_L_87_02', '01_VIHUB1.2_B4_L_87_03', '01_VIHUB1.2_B4_L_88_01', '01_VIHUB1.2_B4_L_88_02', '01_VIHUB1.2_B4_L_88_03', '01_VIHUB1.2_B4_L_89_01', '01_VIHUB1.2_B4_L_89_02', '01_VIHUB1.2_B4_L_89_03', '01_VIHUB1.2_B4_L_90_01', '01_VIHUB1.2_B4_L_90_02',
                        '01_VIHUB1.2_B4_L_91_01', '01_VIHUB1.2_B4_L_92_01', '01_VIHUB1.2_B4_L_92_02', '01_VIHUB1.2_B4_L_92_03', '01_VIHUB1.2_B4_L_92_04', '01_VIHUB1.2_B4_L_92_05', '01_VIHUB1.2_B4_L_93_01',
                        '01_VIHUB1.2_B4_L_94_01', '01_VIHUB1.2_B4_L_94_02', '01_VIHUB1.2_B4_L_94_03', '01_VIHUB1.2_B4_L_94_04', '01_VIHUB1.2_B4_L_94_05', '01_VIHUB1.2_B4_L_95_01', '01_VIHUB1.2_B4_L_95_02', '01_VIHUB1.2_B4_L_95_03', '01_VIHUB1.2_B4_L_95_04', '01_VIHUB1.2_B4_L_96_01', '01_VIHUB1.2_B4_L_96_02',
                        '01_VIHUB1.2_B4_L_98_01', '01_VIHUB1.2_B4_L_98_02', '01_VIHUB1.2_B4_L_99_01', '01_VIHUB1.2_B4_L_100_01', '01_VIHUB1.2_B4_L_100_02', '01_VIHUB1.2_B4_L_101_01', '01_VIHUB1.2_B4_L_102_01', '01_VIHUB1.2_B4_L_102_02', '01_VIHUB1.2_B4_L_102_03', '01_VIHUB1.2_B4_L_103_01', '01_VIHUB1.2_B4_L_104_01',
                        '01_VIHUB1.2_B4_L_105_01', '01_VIHUB1.2_B4_L_105_02', '01_VIHUB1.2_B4_L_105_03', '01_VIHUB1.2_B4_L_105_04', '01_VIHUB1.2_B4_L_106_01', '01_VIHUB1.2_B4_L_107_01', '01_VIHUB1.2_B4_L_107_02',
                        '01_VIHUB1.2_B4_L_108_01', '01_VIHUB1.2_B4_L_108_02', '01_VIHUB1.2_B4_L_108_03', '01_VIHUB1.2_B4_L_108_04', '01_VIHUB1.2_B4_L_108_05', '01_VIHUB1.2_B4_L_109_01', '01_VIHUB1.2_B4_L_110_01', '01_VIHUB1.2_B4_L_110_02', '01_VIHUB1.2_B4_L_110_03', '01_VIHUB1.2_B4_L_110_04',
                        '01_VIHUB1.2_B4_L_111_01', '01_VIHUB1.2_B4_L_111_02', '01_VIHUB1.2_B4_L_111_03', '01_VIHUB1.2_B4_L_112_01', '01_VIHUB1.2_B4_L_113_01', '01_VIHUB1.2_B4_L_113_02', '01_VIHUB1.2_B4_L_114_01', '01_VIHUB1.2_B4_L_114_02', '01_VIHUB1.2_B4_L_115_01', '01_VIHUB1.2_B4_L_115_02',
                        '01_VIHUB1.2_B4_L_116_01', '01_VIHUB1.2_B4_L_116_02', '01_VIHUB1.2_B4_L_117_01', '01_VIHUB1.2_B4_L_117_02', '01_VIHUB1.2_B4_L_117_03', '01_VIHUB1.2_B4_L_118_01', '01_VIHUB1.2_B4_L_118_02', '01_VIHUB1.2_B4_L_118_03', '01_VIHUB1.2_B4_L_119_01',
                        '01_VIHUB1.2_B4_L_120_01', '01_VIHUB1.2_B4_L_120_02', '01_VIHUB1.2_B4_L_120_03', '01_VIHUB1.2_B4_L_120_04', '01_VIHUB1.2_B4_L_120_05', '01_VIHUB1.2_B4_L_121_01', '01_VIHUB1.2_B4_L_121_02', '01_VIHUB1.2_B4_L_121_03',
                        '01_VIHUB1.2_B4_L_122_01', '01_VIHUB1.2_B4_L_122_02', '01_VIHUB1.2_B4_L_122_03', '01_VIHUB1.2_B4_L_123_01', '01_VIHUB1.2_B4_L_123_02', '01_VIHUB1.2_B4_L_124_01', '01_VIHUB1.2_B4_L_124_02', '01_VIHUB1.2_B4_L_125_01', '01_VIHUB1.2_B4_L_125_02',
                        '01_VIHUB1.2_B4_L_126_01', '01_VIHUB1.2_B4_L_126_02', '01_VIHUB1.2_B4_L_126_03', '01_VIHUB1.2_B4_L_127_01', '01_VIHUB1.2_B4_L_127_02', '01_VIHUB1.2_B4_L_127_03', '01_VIHUB1.2_B4_L_127_04',
                        '01_VIHUB1.2_B4_L_128_01', '01_VIHUB1.2_B4_L_128_02', '01_VIHUB1.2_B4_L_128_03', '01_VIHUB1.2_B4_L_128_04', '01_VIHUB1.2_B4_L_128_05', '01_VIHUB1.2_B4_L_129_01', '01_VIHUB1.2_B4_L_129_02', '01_VIHUB1.2_B4_L_129_03', '01_VIHUB1.2_B4_L_129_04', '01_VIHUB1.2_B4_L_129_05', '01_VIHUB1.2_B4_L_129_06', '01_VIHUB1.2_B4_L_130_01',
                        '01_VIHUB1.2_B4_L_131_01', '01_VIHUB1.2_B4_L_131_02', '01_VIHUB1.2_B4_L_131_03', '01_VIHUB1.2_B4_L_131_04', '01_VIHUB1.2_B4_L_131_05', '01_VIHUB1.2_B4_L_132_01', '01_VIHUB1.2_B4_L_133_01', '01_VIHUB1.2_B4_L_134_01', '01_VIHUB1.2_B4_L_134_02', '01_VIHUB1.2_B4_L_135_01',
                        '01_VIHUB1.2_B4_L_136_01', '01_VIHUB1.2_B4_L_137_01', '01_VIHUB1.2_B4_L_138_01', '01_VIHUB1.2_B4_L_138_02', '01_VIHUB1.2_B4_L_138_03', '01_VIHUB1.2_B4_L_138_04', '01_VIHUB1.2_B4_L_139_01', '01_VIHUB1.2_B4_L_139_02', '01_VIHUB1.2_B4_L_140_01', '01_VIHUB1.2_B4_L_140_02',
                        '01_VIHUB1.2_B4_L_141_01', '01_VIHUB1.2_B4_L_141_02', '01_VIHUB1.2_B4_L_141_03', '01_VIHUB1.2_B4_L_141_04', '01_VIHUB1.2_B4_L_141_05', '01_VIHUB1.2_B4_L_142_01', '01_VIHUB1.2_B4_L_143_01', '01_VIHUB1.2_B4_L_144_01', '01_VIHUB1.2_B4_L_144_02', '01_VIHUB1.2_B4_L_145_01', '01_VIHUB1.2_B4_L_145_02',
                        '01_VIHUB1.2_B4_L_145_03', '01_VIHUB1.2_B4_L_145_04', '01_VIHUB1.2_B4_L_146_01', '01_VIHUB1.2_B4_L_146_02', '01_VIHUB1.2_B4_L_147_01', '01_VIHUB1.2_B4_L_147_02', '01_VIHUB1.2_B4_L_147_03', '01_VIHUB1.2_B4_L_148_01', '01_VIHUB1.2_B4_L_149_01', '01_VIHUB1.2_B4_L_149_02', '01_VIHUB1.2_B4_L_149_03', '01_VIHUB1.2_B4_L_149_04',
                        '01_VIHUB1.2_B4_L_150_01', '01_VIHUB1.2_B4_L_150_02', '01_VIHUB1.2_B4_L_150_03', '01_VIHUB1.2_B4_L_150_04', '01_VIHUB1.2_B4_L_151_01', '01_VIHUB1.2_B4_L_151_02', '01_VIHUB1.2_B4_L_152_01', '01_VIHUB1.2_B4_L_152_02', '01_VIHUB1.2_B4_L_153_01', '01_VIHUB1.2_B4_L_153_02',
                        '01_VIHUB1.2_B4_L_154_01', '01_VIHUB1.2_B4_L_154_02', '01_VIHUB1.2_B4_L_154_03', '01_VIHUB1.2_B4_L_155_01', '01_VIHUB1.2_B4_L_155_02']


train_videos = {
    '1': ['01_VIHUB1.2_A9_L_2', '01_VIHUB1.2_A9_L_3', '01_VIHUB1.2_A9_L_4', '01_VIHUB1.2_A9_L_5', '01_VIHUB1.2_A9_L_13', '01_VIHUB1.2_A9_L_14', '01_VIHUB1.2_A9_L_15', '01_VIHUB1.2_A9_L_16', '01_VIHUB1.2_A9_L_18', '01_VIHUB1.2_A9_L_22', '01_VIHUB1.2_A9_L_23', '01_VIHUB1.2_A9_L_24', '01_VIHUB1.2_A9_L_25', '01_VIHUB1.2_A9_L_26', '01_VIHUB1.2_A9_L_27', '01_VIHUB1.2_A9_L_29', '01_VIHUB1.2_A9_L_30', '01_VIHUB1.2_A9_L_31', '01_VIHUB1.2_A9_L_32', '01_VIHUB1.2_A9_L_34', '01_VIHUB1.2_A9_L_35', '01_VIHUB1.2_A9_L_36', '01_VIHUB1.2_A9_L_37', '01_VIHUB1.2_A9_L_39', '01_VIHUB1.2_A9_L_41', '01_VIHUB1.2_A9_L_42', '01_VIHUB1.2_A9_L_43', '01_VIHUB1.2_A9_L_44', '01_VIHUB1.2_A9_L_46', '01_VIHUB1.2_A9_L_49', '01_VIHUB1.2_A9_L_50', '01_VIHUB1.2_A9_L_52', '01_VIHUB1.2_A9_L_53', '01_VIHUB1.2_B4_L_2', '01_VIHUB1.2_B4_L_3', '01_VIHUB1.2_B4_L_5', '01_VIHUB1.2_B4_L_6', '01_VIHUB1.2_B4_L_7', '01_VIHUB1.2_B4_L_10', '01_VIHUB1.2_B4_L_11', '01_VIHUB1.2_B4_L_12', '01_VIHUB1.2_B4_L_13', '01_VIHUB1.2_B4_L_14', '01_VIHUB1.2_B4_L_15', '01_VIHUB1.2_B4_L_17', '01_VIHUB1.2_B4_L_18', '01_VIHUB1.2_B4_L_19', '01_VIHUB1.2_B4_L_20', '01_VIHUB1.2_B4_L_21', '01_VIHUB1.2_B4_L_22', '01_VIHUB1.2_B4_L_23', '01_VIHUB1.2_B4_L_24', '01_VIHUB1.2_B4_L_25', '01_VIHUB1.2_B4_L_26', '01_VIHUB1.2_B4_L_27', '01_VIHUB1.2_B4_L_30', '01_VIHUB1.2_B4_L_31', '01_VIHUB1.2_B4_L_33', '01_VIHUB1.2_B4_L_34', '01_VIHUB1.2_B4_L_35', '01_VIHUB1.2_B4_L_36', '01_VIHUB1.2_B4_L_37', '01_VIHUB1.2_B4_L_76', '01_VIHUB1.2_B4_L_77', '01_VIHUB1.2_B4_L_80', '01_VIHUB1.2_B4_L_81', '01_VIHUB1.2_B4_L_82', '01_VIHUB1.2_B4_L_83', '01_VIHUB1.2_B4_L_84', '01_VIHUB1.2_B4_L_85', '01_VIHUB1.2_B4_L_86', '01_VIHUB1.2_B4_L_88', '01_VIHUB1.2_B4_L_89', '01_VIHUB1.2_B4_L_90', '01_VIHUB1.2_B4_L_91', '01_VIHUB1.2_B4_L_92', '01_VIHUB1.2_B4_L_93', '01_VIHUB1.2_B4_L_95', '01_VIHUB1.2_B4_L_96', '01_VIHUB1.2_B4_L_99', '01_VIHUB1.2_B4_L_101', '01_VIHUB1.2_B4_L_102', '01_VIHUB1.2_B4_L_104', '01_VIHUB1.2_B4_L_105', '01_VIHUB1.2_B4_L_107', '01_VIHUB1.2_B4_L_109', '01_VIHUB1.2_B4_L_110', '01_VIHUB1.2_B4_L_111', '01_VIHUB1.2_B4_L_112', '01_VIHUB1.2_B4_L_113', '01_VIHUB1.2_B4_L_114', '01_VIHUB1.2_B4_L_115', '01_VIHUB1.2_B4_L_116', '01_VIHUB1.2_B4_L_117', '01_VIHUB1.2_B4_L_118', '01_VIHUB1.2_B4_L_119', '01_VIHUB1.2_B4_L_122', '01_VIHUB1.2_B4_L_123', '01_VIHUB1.2_B4_L_124', '01_VIHUB1.2_B4_L_125', '01_VIHUB1.2_B4_L_126', '01_VIHUB1.2_B4_L_128', '01_VIHUB1.2_B4_L_129', '01_VIHUB1.2_B4_L_132', '01_VIHUB1.2_B4_L_133', '01_VIHUB1.2_B4_L_135', '01_VIHUB1.2_B4_L_137', '01_VIHUB1.2_B4_L_138', '01_VIHUB1.2_B4_L_140', '01_VIHUB1.2_B4_L_141', '01_VIHUB1.2_B4_L_142', '01_VIHUB1.2_B4_L_144', '01_VIHUB1.2_B4_L_145', '01_VIHUB1.2_B4_L_146', '01_VIHUB1.2_B4_L_147', '01_VIHUB1.2_B4_L_148', '01_VIHUB1.2_B4_L_152', '01_VIHUB1.2_B4_L_153', '01_VIHUB1.2_B4_L_154', '01_VIHUB1.2_B4_L_155', '01_VIHUB1.2_B5_L_9', '04_GS4_99_L_1', '04_GS4_99_L_2', '04_GS4_99_L_5', '04_GS4_99_L_6', '04_GS4_99_L_7', '04_GS4_99_L_8', '04_GS4_99_L_9', '04_GS4_99_L_10', '04_GS4_99_L_13', '04_GS4_99_L_14', '04_GS4_99_L_18', '04_GS4_99_L_19', '04_GS4_99_L_20', '04_GS4_99_L_21', '04_GS4_99_L_22', '04_GS4_99_L_25', '04_GS4_99_L_27', '04_GS4_99_L_28', '04_GS4_99_L_29', '04_GS4_99_L_30', '04_GS4_99_L_32', '04_GS4_99_L_34', '04_GS4_99_L_36', '04_GS4_99_L_37', '04_GS4_99_L_38', '04_GS4_99_L_41', '04_GS4_99_L_43', '04_GS4_99_L_44', '04_GS4_99_L_45', '04_GS4_99_L_50', '04_GS4_99_L_51', '04_GS4_99_L_52', '04_GS4_99_L_53', '04_GS4_99_L_55', '04_GS4_99_L_56', '04_GS4_99_L_57', '04_GS4_99_L_59', '04_GS4_99_L_60', '04_GS4_99_L_62', '04_GS4_99_L_63', '04_GS4_99_L_64', '04_GS4_99_L_67', '04_GS4_99_L_68', '04_GS4_99_L_69', '04_GS4_99_L_70', '04_GS4_99_L_73', '04_GS4_99_L_74', '04_GS4_99_L_75', '04_GS4_99_L_76', '04_GS4_99_L_77', '04_GS4_99_L_80', '04_GS4_99_L_81', '04_GS4_99_L_83', '04_GS4_99_L_84', '04_GS4_99_L_85', '04_GS4_99_L_86', '04_GS4_99_L_87', '04_GS4_99_L_88', '04_GS4_99_L_90', '04_GS4_99_L_91', '04_GS4_99_L_92', '04_GS4_99_L_97', '04_GS4_99_L_100', '04_GS4_99_L_101', '04_GS4_99_L_105', '04_GS4_99_L_109', '04_GS4_99_L_110', '04_GS4_99_L_111', '04_GS4_99_L_112', '04_GS4_99_L_113', '04_GS4_99_L_115', '04_GS4_99_L_116', '04_GS4_99_L_117', '04_GS4_99_L_118', '04_GS4_99_L_121', '04_GS4_99_L_122', '04_GS4_99_L_123', '04_GS4_99_L_124', '04_GS4_99_L_127'],
    '2': ['01_VIHUB1.2_A9_L_2', '01_VIHUB1.2_A9_L_3', '01_VIHUB1.2_A9_L_4', '01_VIHUB1.2_A9_L_13', '01_VIHUB1.2_A9_L_14', '01_VIHUB1.2_A9_L_15', '01_VIHUB1.2_A9_L_16', '01_VIHUB1.2_A9_L_22', '01_VIHUB1.2_A9_L_23', '01_VIHUB1.2_A9_L_25', '01_VIHUB1.2_A9_L_26', '01_VIHUB1.2_A9_L_29', '01_VIHUB1.2_A9_L_31', '01_VIHUB1.2_A9_L_32', '01_VIHUB1.2_A9_L_34', '01_VIHUB1.2_A9_L_36', '01_VIHUB1.2_A9_L_37', '01_VIHUB1.2_A9_L_39', '01_VIHUB1.2_A9_L_41', '01_VIHUB1.2_A9_L_42', '01_VIHUB1.2_A9_L_43', '01_VIHUB1.2_A9_L_44', '01_VIHUB1.2_A9_L_46', '01_VIHUB1.2_A9_L_49', '01_VIHUB1.2_A9_L_50', '01_VIHUB1.2_A9_L_52', '01_VIHUB1.2_A9_L_53', '01_VIHUB1.2_B4_L_3', '01_VIHUB1.2_B4_L_5', '01_VIHUB1.2_B4_L_10', '01_VIHUB1.2_B4_L_11', '01_VIHUB1.2_B4_L_13', '01_VIHUB1.2_B4_L_14', '01_VIHUB1.2_B4_L_15', '01_VIHUB1.2_B4_L_18', '01_VIHUB1.2_B4_L_19', '01_VIHUB1.2_B4_L_21', '01_VIHUB1.2_B4_L_23', '01_VIHUB1.2_B4_L_25', '01_VIHUB1.2_B4_L_27', '01_VIHUB1.2_B4_L_30', '01_VIHUB1.2_B4_L_31', '01_VIHUB1.2_B4_L_33', '01_VIHUB1.2_B4_L_34', '01_VIHUB1.2_B4_L_35', '01_VIHUB1.2_B4_L_36', '01_VIHUB1.2_B4_L_37', '01_VIHUB1.2_B4_L_77', '01_VIHUB1.2_B4_L_80', '01_VIHUB1.2_B4_L_81', '01_VIHUB1.2_B4_L_83', '01_VIHUB1.2_B4_L_85', '01_VIHUB1.2_B4_L_88', '01_VIHUB1.2_B4_L_89', '01_VIHUB1.2_B4_L_92', '01_VIHUB1.2_B4_L_93', '01_VIHUB1.2_B4_L_95', '01_VIHUB1.2_B4_L_96', '01_VIHUB1.2_B4_L_99', '01_VIHUB1.2_B4_L_101', '01_VIHUB1.2_B4_L_102', '01_VIHUB1.2_B4_L_104', '01_VIHUB1.2_B4_L_105', '01_VIHUB1.2_B4_L_109', '01_VIHUB1.2_B4_L_110', '01_VIHUB1.2_B4_L_112', '01_VIHUB1.2_B4_L_114', '01_VIHUB1.2_B4_L_116', '01_VIHUB1.2_B4_L_117', '01_VIHUB1.2_B4_L_118', '01_VIHUB1.2_B4_L_119', '01_VIHUB1.2_B4_L_122', '01_VIHUB1.2_B4_L_124', '01_VIHUB1.2_B4_L_125', '01_VIHUB1.2_B4_L_126', '01_VIHUB1.2_B4_L_128', '01_VIHUB1.2_B4_L_129', '01_VIHUB1.2_B4_L_132', '01_VIHUB1.2_B4_L_133', '01_VIHUB1.2_B4_L_135', '01_VIHUB1.2_B4_L_138', '01_VIHUB1.2_B4_L_140', '01_VIHUB1.2_B4_L_141', '01_VIHUB1.2_B4_L_142', '01_VIHUB1.2_B4_L_145', '01_VIHUB1.2_B4_L_147', '01_VIHUB1.2_B4_L_148', '01_VIHUB1.2_B4_L_154', '01_VIHUB1.2_B4_L_155', '04_GS4_99_L_1', '04_GS4_99_L_2', '04_GS4_99_L_5', '04_GS4_99_L_6', '04_GS4_99_L_8', '04_GS4_99_L_9', '04_GS4_99_L_10', '04_GS4_99_L_13', '04_GS4_99_L_14', '04_GS4_99_L_18', '04_GS4_99_L_19', '04_GS4_99_L_20', '04_GS4_99_L_21', '04_GS4_99_L_22', '04_GS4_99_L_25', '04_GS4_99_L_27', '04_GS4_99_L_30', '04_GS4_99_L_32', '04_GS4_99_L_34', '04_GS4_99_L_36', '04_GS4_99_L_41', '04_GS4_99_L_43', '04_GS4_99_L_45', '04_GS4_99_L_51', '04_GS4_99_L_52', '04_GS4_99_L_53', '04_GS4_99_L_55', '04_GS4_99_L_56', '04_GS4_99_L_57', '04_GS4_99_L_62', '04_GS4_99_L_63', '04_GS4_99_L_67', '04_GS4_99_L_68', '04_GS4_99_L_69', '04_GS4_99_L_70', '04_GS4_99_L_73', '04_GS4_99_L_74', '04_GS4_99_L_76', '04_GS4_99_L_77', '04_GS4_99_L_80', '04_GS4_99_L_81', '04_GS4_99_L_83', '04_GS4_99_L_85', '04_GS4_99_L_90', '04_GS4_99_L_91', '04_GS4_99_L_97', '04_GS4_99_L_100', '04_GS4_99_L_101', '04_GS4_99_L_105', '04_GS4_99_L_109', '04_GS4_99_L_110', '04_GS4_99_L_111', '04_GS4_99_L_112', '04_GS4_99_L_113', '04_GS4_99_L_115', '04_GS4_99_L_118', '04_GS4_99_L_121', '04_GS4_99_L_122', '04_GS4_99_L_123', '04_GS4_99_L_124', '04_GS4_99_L_127']
}

val_videos = {
      '1': ['01_VIHUB1.2_A9_L_6', '01_VIHUB1.2_A9_L_19', '01_VIHUB1.2_A9_L_20', '01_VIHUB1.2_A9_L_21', '01_VIHUB1.2_A9_L_38', '01_VIHUB1.2_A9_L_40', '01_VIHUB1.2_A9_L_47', '01_VIHUB1.2_A9_L_48', '01_VIHUB1.2_A9_L_51', '01_VIHUB1.2_B4_L_1', '01_VIHUB1.2_B4_L_4', '01_VIHUB1.2_B4_L_8', '01_VIHUB1.2_B4_L_9', '01_VIHUB1.2_B4_L_16', '01_VIHUB1.2_B4_L_28', '01_VIHUB1.2_B4_L_29', '01_VIHUB1.2_B4_L_75', '01_VIHUB1.2_B4_L_87', '01_VIHUB1.2_B4_L_94', '01_VIHUB1.2_B4_L_98', '01_VIHUB1.2_B4_L_100', '01_VIHUB1.2_B4_L_103', '01_VIHUB1.2_B4_L_106', '01_VIHUB1.2_B4_L_108', '01_VIHUB1.2_B4_L_120', '01_VIHUB1.2_B4_L_121', '01_VIHUB1.2_B4_L_127', '01_VIHUB1.2_B4_L_130', '01_VIHUB1.2_B4_L_131', '01_VIHUB1.2_B4_L_134', '01_VIHUB1.2_B4_L_136', '01_VIHUB1.2_B4_L_139', '01_VIHUB1.2_B4_L_143', '01_VIHUB1.2_B4_L_149', '01_VIHUB1.2_B4_L_150', '01_VIHUB1.2_B4_L_151', '04_GS4_99_L_3', '04_GS4_99_L_4', '04_GS4_99_L_11', '04_GS4_99_L_12', '04_GS4_99_L_16', '04_GS4_99_L_17', '04_GS4_99_L_26', '04_GS4_99_L_39', '04_GS4_99_L_40', '04_GS4_99_L_42', '04_GS4_99_L_46', '04_GS4_99_L_48', '04_GS4_99_L_49', '04_GS4_99_L_58', '04_GS4_99_L_61', '04_GS4_99_L_65', '04_GS4_99_L_66', '04_GS4_99_L_71', '04_GS4_99_L_72', '04_GS4_99_L_79', '04_GS4_99_L_82', '04_GS4_99_L_89', '04_GS4_99_L_94', '04_GS4_99_L_95', '04_GS4_99_L_96', '04_GS4_99_L_98', '04_GS4_99_L_99', '04_GS4_99_L_102', '04_GS4_99_L_103', '04_GS4_99_L_104', '04_GS4_99_L_106', '04_GS4_99_L_107', '04_GS4_99_L_108', '04_GS4_99_L_114', '04_GS4_99_L_120', '04_GS4_99_L_125', '04_GS4_99_L_126'],
    '2': ['01_VIHUB1.2_A9_L_5', '01_VIHUB1.2_A9_L_6', '01_VIHUB1.2_A9_L_18', '01_VIHUB1.2_A9_L_19', '01_VIHUB1.2_A9_L_20', '01_VIHUB1.2_A9_L_21', '01_VIHUB1.2_A9_L_24', '01_VIHUB1.2_A9_L_27', '01_VIHUB1.2_A9_L_30', '01_VIHUB1.2_A9_L_35', '01_VIHUB1.2_A9_L_38', '01_VIHUB1.2_A9_L_40', '01_VIHUB1.2_A9_L_47', '01_VIHUB1.2_A9_L_48', '01_VIHUB1.2_A9_L_51', '01_VIHUB1.2_B4_L_1', '01_VIHUB1.2_B4_L_2', '01_VIHUB1.2_B4_L_4', '01_VIHUB1.2_B4_L_6', '01_VIHUB1.2_B4_L_7', '01_VIHUB1.2_B4_L_8', '01_VIHUB1.2_B4_L_9', '01_VIHUB1.2_B4_L_12', '01_VIHUB1.2_B4_L_16', '01_VIHUB1.2_B4_L_17', '01_VIHUB1.2_B4_L_20', '01_VIHUB1.2_B4_L_22', '01_VIHUB1.2_B4_L_24', '01_VIHUB1.2_B4_L_26', '01_VIHUB1.2_B4_L_28', '01_VIHUB1.2_B4_L_29', '01_VIHUB1.2_B4_L_75', '01_VIHUB1.2_B4_L_76', '01_VIHUB1.2_B4_L_82', '01_VIHUB1.2_B4_L_84', '01_VIHUB1.2_B4_L_86', '01_VIHUB1.2_B4_L_87', '01_VIHUB1.2_B4_L_90', '01_VIHUB1.2_B4_L_91', '01_VIHUB1.2_B4_L_94', '01_VIHUB1.2_B4_L_98', '01_VIHUB1.2_B4_L_100', '01_VIHUB1.2_B4_L_103', '01_VIHUB1.2_B4_L_106', '01_VIHUB1.2_B4_L_107', '01_VIHUB1.2_B4_L_108', '01_VIHUB1.2_B4_L_111', '01_VIHUB1.2_B4_L_113', '01_VIHUB1.2_B4_L_115', '01_VIHUB1.2_B4_L_120', '01_VIHUB1.2_B4_L_121', '01_VIHUB1.2_B4_L_123', '01_VIHUB1.2_B4_L_127', '01_VIHUB1.2_B4_L_130', '01_VIHUB1.2_B4_L_131', '01_VIHUB1.2_B4_L_134', '01_VIHUB1.2_B4_L_136', '01_VIHUB1.2_B4_L_137', '01_VIHUB1.2_B4_L_139', '01_VIHUB1.2_B4_L_143', '01_VIHUB1.2_B4_L_144', '01_VIHUB1.2_B4_L_146', '01_VIHUB1.2_B4_L_149', '01_VIHUB1.2_B4_L_150', '01_VIHUB1.2_B4_L_151', '01_VIHUB1.2_B4_L_152', '01_VIHUB1.2_B4_L_153', '01_VIHUB1.2_B5_L_9', '04_GS4_99_L_3', '04_GS4_99_L_4', '04_GS4_99_L_7', '04_GS4_99_L_11', '04_GS4_99_L_12', '04_GS4_99_L_16', '04_GS4_99_L_17', '04_GS4_99_L_26', '04_GS4_99_L_28', '04_GS4_99_L_29', '04_GS4_99_L_37', '04_GS4_99_L_38', '04_GS4_99_L_39', '04_GS4_99_L_40', '04_GS4_99_L_42', '04_GS4_99_L_44', '04_GS4_99_L_46', '04_GS4_99_L_48', '04_GS4_99_L_49', '04_GS4_99_L_50', '04_GS4_99_L_58', '04_GS4_99_L_59', '04_GS4_99_L_60', '04_GS4_99_L_61', '04_GS4_99_L_64', '04_GS4_99_L_65', '04_GS4_99_L_66', '04_GS4_99_L_71', '04_GS4_99_L_72', '04_GS4_99_L_75', '04_GS4_99_L_79', '04_GS4_99_L_82', '04_GS4_99_L_84', '04_GS4_99_L_86', '04_GS4_99_L_87', '04_GS4_99_L_88', '04_GS4_99_L_89', '04_GS4_99_L_92', '04_GS4_99_L_94', '04_GS4_99_L_95', '04_GS4_99_L_96', '04_GS4_99_L_98', '04_GS4_99_L_99', '04_GS4_99_L_102', '04_GS4_99_L_103', '04_GS4_99_L_104', '04_GS4_99_L_106', '04_GS4_99_L_107', '04_GS4_99_L_108', '04_GS4_99_L_114', '04_GS4_99_L_116', '04_GS4_99_L_117', '04_GS4_99_L_120', '04_GS4_99_L_125', '04_GS4_99_L_126'],
    'all': ['01_VIHUB1.2_A9_L_6', '01_VIHUB1.2_A9_L_19', '01_VIHUB1.2_A9_L_20', '01_VIHUB1.2_A9_L_21', '01_VIHUB1.2_A9_L_38', '01_VIHUB1.2_A9_L_40', '01_VIHUB1.2_A9_L_47', '01_VIHUB1.2_A9_L_48', '01_VIHUB1.2_A9_L_51', '01_VIHUB1.2_B4_L_1', '01_VIHUB1.2_B4_L_4', '01_VIHUB1.2_B4_L_8', '01_VIHUB1.2_B4_L_9', '01_VIHUB1.2_B4_L_16', '01_VIHUB1.2_B4_L_28', '01_VIHUB1.2_B4_L_29', '01_VIHUB1.2_B4_L_75', '01_VIHUB1.2_B4_L_87', '01_VIHUB1.2_B4_L_94', '01_VIHUB1.2_B4_L_98', '01_VIHUB1.2_B4_L_100', '01_VIHUB1.2_B4_L_103', '01_VIHUB1.2_B4_L_106', '01_VIHUB1.2_B4_L_108', '01_VIHUB1.2_B4_L_120', '01_VIHUB1.2_B4_L_121', '01_VIHUB1.2_B4_L_127', '01_VIHUB1.2_B4_L_130', '01_VIHUB1.2_B4_L_131', '01_VIHUB1.2_B4_L_134', '01_VIHUB1.2_B4_L_136', '01_VIHUB1.2_B4_L_139', '01_VIHUB1.2_B4_L_143', '01_VIHUB1.2_B4_L_149', '01_VIHUB1.2_B4_L_150', '01_VIHUB1.2_B4_L_151', '04_GS4_99_L_3', '04_GS4_99_L_4', '04_GS4_99_L_11', '04_GS4_99_L_12', '04_GS4_99_L_16', '04_GS4_99_L_17', '04_GS4_99_L_26', '04_GS4_99_L_39', '04_GS4_99_L_40', '04_GS4_99_L_42', '04_GS4_99_L_46', '04_GS4_99_L_48', '04_GS4_99_L_49', '04_GS4_99_L_58', '04_GS4_99_L_61', '04_GS4_99_L_65', '04_GS4_99_L_66', '04_GS4_99_L_71', '04_GS4_99_L_72', '04_GS4_99_L_79', '04_GS4_99_L_82', '04_GS4_99_L_89', '04_GS4_99_L_94', '04_GS4_99_L_95', '04_GS4_99_L_96', '04_GS4_99_L_98', '04_GS4_99_L_99', '04_GS4_99_L_102', '04_GS4_99_L_103', '04_GS4_99_L_104', '04_GS4_99_L_106', '04_GS4_99_L_107', '04_GS4_99_L_108', '04_GS4_99_L_114', '04_GS4_99_L_120', '04_GS4_99_L_125', '04_GS4_99_L_126'] + ['01_VIHUB1.2_A9_L_5', '01_VIHUB1.2_A9_L_6', '01_VIHUB1.2_A9_L_18', '01_VIHUB1.2_A9_L_19', '01_VIHUB1.2_A9_L_20', '01_VIHUB1.2_A9_L_21', '01_VIHUB1.2_A9_L_24', '01_VIHUB1.2_A9_L_27', '01_VIHUB1.2_A9_L_30', '01_VIHUB1.2_A9_L_35', '01_VIHUB1.2_A9_L_38', '01_VIHUB1.2_A9_L_40', '01_VIHUB1.2_A9_L_47', '01_VIHUB1.2_A9_L_48', '01_VIHUB1.2_A9_L_51', '01_VIHUB1.2_B4_L_1', '01_VIHUB1.2_B4_L_2', '01_VIHUB1.2_B4_L_4', '01_VIHUB1.2_B4_L_6', '01_VIHUB1.2_B4_L_7', '01_VIHUB1.2_B4_L_8', '01_VIHUB1.2_B4_L_9', '01_VIHUB1.2_B4_L_12', '01_VIHUB1.2_B4_L_16', '01_VIHUB1.2_B4_L_17', '01_VIHUB1.2_B4_L_20', '01_VIHUB1.2_B4_L_22', '01_VIHUB1.2_B4_L_24', '01_VIHUB1.2_B4_L_26', '01_VIHUB1.2_B4_L_28', '01_VIHUB1.2_B4_L_29', '01_VIHUB1.2_B4_L_75', '01_VIHUB1.2_B4_L_76', '01_VIHUB1.2_B4_L_82', '01_VIHUB1.2_B4_L_84', '01_VIHUB1.2_B4_L_86', '01_VIHUB1.2_B4_L_87', '01_VIHUB1.2_B4_L_90', '01_VIHUB1.2_B4_L_91', '01_VIHUB1.2_B4_L_94', '01_VIHUB1.2_B4_L_98', '01_VIHUB1.2_B4_L_100', '01_VIHUB1.2_B4_L_103', '01_VIHUB1.2_B4_L_106', '01_VIHUB1.2_B4_L_107', '01_VIHUB1.2_B4_L_108', '01_VIHUB1.2_B4_L_111', '01_VIHUB1.2_B4_L_113', '01_VIHUB1.2_B4_L_115', '01_VIHUB1.2_B4_L_120', '01_VIHUB1.2_B4_L_121', '01_VIHUB1.2_B4_L_123', '01_VIHUB1.2_B4_L_127', '01_VIHUB1.2_B4_L_130', '01_VIHUB1.2_B4_L_131', '01_VIHUB1.2_B4_L_134', '01_VIHUB1.2_B4_L_136', '01_VIHUB1.2_B4_L_137', '01_VIHUB1.2_B4_L_139', '01_VIHUB1.2_B4_L_143', '01_VIHUB1.2_B4_L_144', '01_VIHUB1.2_B4_L_146', '01_VIHUB1.2_B4_L_149', '01_VIHUB1.2_B4_L_150', '01_VIHUB1.2_B4_L_151', '01_VIHUB1.2_B4_L_152', '01_VIHUB1.2_B4_L_153', '01_VIHUB1.2_B5_L_9', '04_GS4_99_L_3', '04_GS4_99_L_4', '04_GS4_99_L_7', '04_GS4_99_L_11', '04_GS4_99_L_12', '04_GS4_99_L_16', '04_GS4_99_L_17', '04_GS4_99_L_26', '04_GS4_99_L_28', '04_GS4_99_L_29', '04_GS4_99_L_37', '04_GS4_99_L_38', '04_GS4_99_L_39', '04_GS4_99_L_40', '04_GS4_99_L_42', '04_GS4_99_L_44', '04_GS4_99_L_46', '04_GS4_99_L_48', '04_GS4_99_L_49', '04_GS4_99_L_50', '04_GS4_99_L_58', '04_GS4_99_L_59', '04_GS4_99_L_60', '04_GS4_99_L_61', '04_GS4_99_L_64', '04_GS4_99_L_65', '04_GS4_99_L_66', '04_GS4_99_L_71', '04_GS4_99_L_72', '04_GS4_99_L_75', '04_GS4_99_L_79', '04_GS4_99_L_82', '04_GS4_99_L_84', '04_GS4_99_L_86', '04_GS4_99_L_87', '04_GS4_99_L_88', '04_GS4_99_L_89', '04_GS4_99_L_92', '04_GS4_99_L_94', '04_GS4_99_L_95', '04_GS4_99_L_96', '04_GS4_99_L_98', '04_GS4_99_L_99', '04_GS4_99_L_102', '04_GS4_99_L_103', '04_GS4_99_L_104', '04_GS4_99_L_106', '04_GS4_99_L_107', '04_GS4_99_L_108', '04_GS4_99_L_114', '04_GS4_99_L_116', '04_GS4_99_L_117', '04_GS4_99_L_120', '04_GS4_99_L_125', '04_GS4_99_L_126'],
    'free': ['01_VIHUB1.2_A9_L_21']
}


video_details = {
      'gangbuksamsung': gangbuk_samsung_videos,
      'severance_1st': severance_1st_videos,
      'severance_2nd': severance_2nd_videos,
      'lapa': gangbuk_samsung_videos + severance_1st_videos + severance_2nd_videos
}