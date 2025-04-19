import os
import json
import load_polygons as lplg
import Save_polygons as splg


class CheckJson:
    def __init__(self):
        
        pass

    # Проверка в settings.json строки "load_polygons_from_file": True
    def check_json_load(self):
        path = os.path.join(os.path.dirname(__file__), 'settings.json')
        with open(os.path.abspath(path)) as stts:
            settings = json.load(stts)
            if not settings.get("load_polygons_from_file"): #проверяем значение в модуле settings.json
                print(f'load_polygons_from_file is False. Check settings.json file')
                return #закончить выполнение программы
        
            if os.path.getsize(os.path.join(os.path.dirname(__file__), 'polygon.json'))!=0: # проверяем пустой ли файл polygon.json
                path = os.path.join(os.path.dirname(__file__), 'polygon.json')
                with open(os.path.abspath(path)) as plg:
                    poligons = json.load(plg)
                    return poligons                          
            else:
                print(f"THE FILE WITH POLYGONS IS UNAVAILABLE OR MISSING OUT. POLYGON'S GENERATION BEGIN")
                return
                
            
            

    # Проверка в settings.json строки "save_polygons_after_generation": True
    def check_json_save(self): 
        if os.path.getsize(os.path.join(os.path.dirname(__file__), 'polygon.json'))==0:
            print()
            path = os.path.join(os.path.dirname(__file__), 'settings.json')
            with open(os.path.abspath(path)) as stts:
                settings=json.load(stts)
                if settings.get('save_polygons_after_generation') == True:
                    from Main import poligons
                    saving = splg.SavePolygons()
                    saving.save(poligons)
                else:
                    return #закончить выполнение программы
        else:
            pass                
