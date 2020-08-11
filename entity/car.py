"""
 @description: 描述汽车
 @auther: 29263
 @date: 2020-08-11 13:05
"""
import datetime


# 功能描述: 汽车具有品牌，车系，出厂日期，里程,价格；
# 能行驶
class Car:
    mileage = 0  # 汽车里程

    def __init__(self, brand, series, production_date, price):
        self.brand = brand
        self.series = series
        self.production_date = production_date
        self.price = price

    def driving(self, mile):
        if mile > 0:
            self.mileage += mile  # 计算总路程
            print(f"本次行驶了{mile}公里，总共行驶了{self.mileage}公里")
        else:
            print("无效里程")

    def introduce(self):
        print(f"产品信息：{self.brand}{self.series},生产日期：{self.production_date}\n在售价：{self.price}")


date = datetime.date(2019, 12, 5)
audi = Car("奥迪", "A3", date, 150000)
audi.introduce()
audi.driving(100)
