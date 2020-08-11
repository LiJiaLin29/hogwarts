"""
 @description: 描述笔记本
 @auther: 29263
 @date: 2020-08-11 13:39
"""


# 功能描述: 笔记本具有品牌，系列，处理器,存储容量，价格；
class Computer:

    def __init__(self, brand, series, cpu, memory, price):
        self.brand = brand
        self.series = series
        self.cpu = cpu
        self.memory = memory
        self.price = price

    def introduce(self):
        print(f"产品信息：{self.brand}{self.series},处理器：{self.cpu},存储：{self.memory/1024}T\n在售价：{self.price}")


mac = Computer("苹果", "Macbook", "ios12.0", 150000, 12999)
mac.introduce()
