
import os
import re
from library import usecsv
import numpy as np
import numpy_financial as npf

class businessAnalze:
    def __init__(self):
        self.presentValue()
        # self.discount = discount
        # self.cashflow = cashflow
        # self.year = n


    def presentValue(self):
        # presentValue = (self.cashflow/((1 + self.discount) ** self.year))
        # print(self.year,"년에 대한" ,"현재 자산가지 :", presentValue)
            # 1. 세부 지표 값 구하기
            loss = [-750, -250]
            profit = [100]*18
            cf = loss+profit
            cashflow = np.array(cf)

            # 2. 순현재가치(NPV)와 내부수익률(IRR) 구하기
            npv = npf.npv(0.045, cashflow)
            irr = npf.irr(cashflow)

            print("순현재가치(npv) : ", npv, "내부수익률(irr) : ", irr)


if __name__ == "__main__":
    businessAnalze()

    # disCount = float(input("할인율을 입력해주세요 : "))
    # cashFlow = float(input("현금흐름을 입력해주세요 : "))
    # n = float(input("확인하고자 하는 최종 연차를 입력해주세요 : "))

    #for i in range(int(n)):
        # businessAnalze = businessAnalze()
        # businessAnalze.presentValue()
