import scrapy


class DiabetesbotSpider(scrapy.Spider):
    name = 'diabetesbot'
    allowed_domains = ['diabetesjournals.org']
    start_urls = [
        'https://diabetesjournals.org/care/article/45/Supplement_1/S8/138915/1-Improving-Care-and-Promoting-Health-in',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S17/138925/2-Classification-and-Diagnosis-of-Diabetes',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S39/138909/3-Prevention-or-Delay-of-Type-2-Diabetes-and',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S46/138926/4-Comprehensive-Medical-Evaluation-and-Assessment',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S60/138923/5-Facilitating-Behavior-Change-and-Well-being-to',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S83/138927/6-Glycemic-Targets-Standards-of-Medical-Care-in',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S97/138911/7-Diabetes-Technology-Standards-of-Medical-Care-in',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S113/138906/8-Obesity-and-Weight-Management-for-the-Prevention',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S125/138908/9-Pharmacologic-Approaches-to-Glycemic-Treatment',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S144/138910/10-Cardiovascular-Disease-and-Risk-Management',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S175/138914/11-Chronic-Kidney-Disease-and-Risk-Management',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S185/138917/12-Retinopathy-Neuropathy-and-Foot-Care-Standards',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S195/138920/13-Older-Adults-Standards-of-Medical-Care-in',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S208/138922/14-Children-and-Adolescents-Standards-of-Medical',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S232/138916/15-Management-of-Diabetes-in-Pregnancy-Standards',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S244/138924/16-Diabetes-Care-in-the-Hospital-Standards-of',
        'https://diabetesjournals.org/care/article/45/Supplement_1/S254/138913/17-Diabetes-Advocacy-Standards-of-Medical-Care-in',
    ]

    def parse(self, response):
        for article in response.css('div.article-section-wrapper'):
            print({
                'content': article.css('div.article-section-wrapper p::text').getall()
            })