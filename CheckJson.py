import os
import json
import load_polygons as lplg
import Save_polygons as splg


class CheckJson:
    # Проверка в settings.json строки "load_polygons_from_file": True
    def check_json_load():
        with open('settings.json') as stts:
            settings = json.load(stts)
            return settings.get("load_polygons_from_file")
                      

    # Проверка в settings.json строки "save_polygons_after_generation": True
    def check_json_save(poligons): 
        with open('settings.json') as stts:
            settings=json.load(stts)
            if settings.get('save_polygons_after_generation') == True:
                saving = splg.SavePolygons()
                saving.save(poligons)
