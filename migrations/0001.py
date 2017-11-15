import models

def forward ():
  models.DB.create_tables([models.Author, models.BlogPost, models.Comment])

if __name__ == '__main__':
  forward()
