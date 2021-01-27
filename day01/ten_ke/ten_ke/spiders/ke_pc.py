import scrapy
import csv

class CourseInfo(scrapy.Item):
    course_name = scrapy.Field()    #课程名称
    course_price = scrapy.Field()   #课程价格
    # course_time=scrapy.Field()  #课程时长
    # course_people=scrapy.Field()    #课程报名人数



    


class KePcSpider(scrapy.Spider):
    pageno=2
    name = 'ke_pc'
    allowed_domains = ['ke.qq.com']
    start_urls = "https://ke.qq.com/course/list?price_min=1&task_filter=0000001&page%d"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }

    def parse(self, response):
        pass

    def start_requests(self):
        print("start.....")
        request=scrapy.Request(
            url=self.start_urls%self.pageno,
            callback=self.parse_ke,
            method="get",
            headers=self.headers,
            errback=self.err_ke
        )
        return [request]

     # 手工提交请求
    def parse_ke(self,response):
        print("开始解析.....")
        output=[]  #结果存放
        all_courses=response.xpath("//html/body/section[1]/div/div[4]/ul/li")
        for course in all_courses:

            course_data=CourseInfo()
            course_data["course_name"] = course.xpath("h4/a/@title").get()
            course_data["course_price"] = course.xpath("div/span[@class='line-cell item-user custom-string']/text()").get().strip()
            course_data["course_time"]=course.xpath()

            output.append(course_data)
        if self.pageno<7:
            self.pageno+=1
            request=scrapy.Request(
            url=self.start_urls%self.pageno,
            callback=self.parse_ke,
            method="get",
            headers=self.headers,
            errback=self.err_ke)
            output.append(request)
        return output
    def err_ke(self,err):
        print("出错或者爬取结束")

    def write_csv(self):
        # 1. 创建文件对象
        f = open('E:/SEU/SEUAI/day01/ten_ke/ten_ke/spiders/ke.csv', 'a', encoding='utf-8', newline="")
    
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
    
        # 3. 构建列表头
        # csv_writer.writerow(["股票名称", "股票代码", "股票价格", "股票成交额"])
    
        # 4. 写入数据
        for i,j in self.output:
            csv_writer.writerow([i,j])
    



        
             
         

