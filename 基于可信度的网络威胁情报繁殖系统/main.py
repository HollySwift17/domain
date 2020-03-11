from collect_data.collect_main import  collect_main
from analysis.new_train_feature import feature
from machine_learning.update_trails import update
from machine_learning.train_models import train_models
from machine_learning.test import test


#collect_main()
#feature()
update()
train_models()
test()
