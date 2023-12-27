import csv


class DoubanPipeline:
    def __init__(self):
        # 打开 CSV 文件并创建 CSV 写入器
        self.csv_file = open('result/douban_movies.csv', 'w',
                             newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)

        # 写入 CSV 文件的标题行
        self.csv_writer.writerow(
            ['Title', 'type', 'directors', 'duration', 'douban_score'])

    def process_item(self, item, spider):
        # 将数据写入 CSV 文件
        self.csv_writer.writerow(
            [item['title'], item['type'], item['directors'], item['duration'], item['douban_score']])
        return item

    def close_spider(self, spider):
        # 在关闭 spider 时关闭 CSV 文件
        self.csv_file.close()


class MovieHrefPipeline():

    def __init__(self):
        # 打开 CSV 文件并创建 CSV 写入器
        self.csv_file = open('result/movie_href.csv', 'w',
                             newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)

        # 写入 CSV 文件的标题行
        self.csv_writer.writerow(['movie_href'])

    def process_item(self, item, spider):
        # 将数据写入 CSV 文件
        self.csv_writer.writerow([item['href']])
        return item

    def close_spider(self, spider):
        # 在关闭 spider 时关闭 CSV 文件
        self.csv_file.close()

class MovieCommentPipeline():

    def __init__(self):
        # 打开 CSV 文件并创建 CSV 写入器
        self.csv_file = open('result/movie_comment.csv', 'w',
                             newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)

        # 写入 CSV 文件的标题行
        self.csv_writer.writerow(['content'])

    def process_item(self, item, spider):
        # 将数据写入 CSV 文件
        self.csv_writer.writerow([item['content']])
        return item

    def close_spider(self, spider):
        # 在关闭 spider 时关闭 CSV 文件
        self.csv_file.close()

