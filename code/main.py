import yaml
import json
from mappingGenerator import MappingGenerator
from CsvProcessor import CsvProcessor 
def readYarrrml(mappingPath):
    data = yaml.load(open(mappingPath), Loader=yaml.FullLoader)
    with open('mapping.json', 'w') as f:
        f.write(json.dumps(data,indent=2))



def main():
    #readYarrrml('../mappings/mapping.yaml')
    csvP = CsvProcessor('../csv/clasificacion-economica-gasto-labels.csv')
    csvP.normalizeCsv()
    # uri = 'http://example.com/'
    # mg1 = MappingGenerator(2,uri + 'taxonomy1')
    # mg2 = MappingGenerator(4, uri + 'taxonomy2')
    # mg3 = MappingGenerator(10, uri + 'taxonomy3')
    # print('**********************MAPPING 2 COLS**********************')
    # mg1.generateMapping(fileName='2cols.yaml')
    # print('**********************MAPPING 4 COLS**********************')
    # mg2.generateMapping(fileName='4cols.yaml')
    # print('**********************MAPPING 10 COLS**********************')
    # mg3.generateMapping(fileName='10cols.yaml')
if __name__ == '__main__':
    main()
