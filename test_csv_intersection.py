import csv_intersection

def test_csv_inteserction():
    result = csv_intersection.get_csv_intersection("test_data/CurrentSPACsasofOctober2020.csv", "test_data/octoberOCCnewoptionmarketunderlyings.csv")
    assert result == ['DPHC', 'FVAC', 'GMHI', 'HCAC', 'IPOB', 'IPOC', 'KCAC', 'PIC', 'PSTH']
    