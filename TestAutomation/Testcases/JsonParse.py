import json

try:
    Dic= '{"k1":"V1","k2":"V2"}'
    jd = json.loads(Dic)
    print(jd["k1"])

except Exception as e:
    print(e)