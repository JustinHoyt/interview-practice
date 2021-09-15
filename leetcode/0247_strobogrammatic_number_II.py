from typing import *

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        results: List[str] = []

        def leading_zero(sofar: str):
            return sofar[0] == '0' and len(sofar) != 1

        def find_strobogrammatic_rec(sofar: str = ''):
            if len(sofar) == n:
                if not leading_zero(sofar):
                    results.append(sofar)
                return

            for left, right in [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]:
                find_strobogrammatic_rec(f'{left}{sofar}{right}')

        if n % 2 == 1:
            for center_num in ['0', '1', '8']:
                find_strobogrammatic_rec(center_num)
        else:
            find_strobogrammatic_rec()
                
        print(results)
        return results


def test_happy_path():
    assert Solution().findStrobogrammatic(2) == ['11', '69', '88', '96']

def test_single_digit():
    assert Solution().findStrobogrammatic(1) == ['0', '1', '8']

def test_three_digits():
    assert Solution().findStrobogrammatic(3) == ['101', '609', '808', '906', '111', '619', '818', '916', '181', '689', '888', '986']

def test_five_digits():
    assert Solution().findStrobogrammatic(5) == ['10001', '60009', '80008', '90006', '11011', '61019', '81018', '91016', '16091', '66099', '86098', '96096', '18081', '68089', '88088', '98086', '19061', '69069', '89068', '99066', '10101', '60109', '80108', '90106', '11111', '61119', '81118', '91116', '16191', '66199', '86198', '96196', '18181', '68189', '88188', '98186', '19161', '69169', '89168', '99166', '10801', '60809', '80808', '90806', '11811', '61819', '81818', '91816', '16891', '66899', '86898', '96896', '18881', '68889', '88888', '98886', '19861', '69869', '89868', '99866']


if __name__ == "__main__":
    test_happy_path()