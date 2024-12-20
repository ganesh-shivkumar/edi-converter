import string

from pymongo import MongoClient
from datetime import datetime

def get_database(database_name : string):
    connection_string = "mongodb+srv://ganny131293:WkLMTB7rsimimmSI@edi855cluster.ame22.mongodb.net/?retryWrites=true&w=majority&appName=EDI855Cluster"
    client = MongoClient(connection_string)
    return client[database_name]


edi855_json_db = get_database("edi855_edi_json_data")
timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data_collection = edi855_json_db["edi855_edi_json_data"]
timestamp_collection = edi855_json_db["timestamp"]

timestamp_1 = {
    "_id" : timestamp_str + "-ts",
    "timestamp" : timestamp_str
}

item_1 = {
    "_id" : timestamp_str + "001",
    "text_input" : "ISA*00*          *00*          *01*197819683      *01*00060902413TST *240919*0650*U*00401*000000131*0*T*|~\nGS*PR*197819683*0060902411A2B*240919*0650*000000131*X*004010~\nST*855*600000482~\nBAK*06*AD*100000*20160922~\nREF*YB*0~\nN9*L1**Notes ~\nMSG*Acknowledge on order received.~\nPO1*1*1234567890.1*EA***BP*86100000~\nPID*F****Test Product 100001~\nACK*IA*1234567890.1*EA*069*20160929~\nN9*L1**Letters or Notes~\nMSG*Acknowledge on order received.~\nCTT*1~\nSE*12*600000482~\nGE*1*000000131~\nIEA*1*000000131~",
    "output" : "{\n  \"purchase_order_header\": {\n    \"order_id\": \"100000\",\n    \"order_revision\": \"0\",\n    \"change_code\": \"NOCHANGE\",\n    \"purpose_code\": \"ACK\",\n    \"purchasing_operating_unit\": {\n      \"operating_unit_id\": \"1A2B\"\n    },\n    \"date_times\": [\n      {\n        \"date_time_type\": \"POD\",\n        \"date_time_value\": {\n          \"seconds\": 1474531200\n        }\n      }\n    ],\n    \"notes\": [\n      {\n        \"note_type\": \"INT\",\n        \"note_value\": \"Acknowledge on order received.\"\n      }\n    ]\n  },\n  \"purchase_order_lines\": [\n    {\n      \"line_id\": \"1\",\n      \"item_details\": [\n        {\n          \"item_type\": \"BITM\",\n          \"item_name\": \"86100000\",\n          \"item_description\": \"Test Product 100001\"\n        }\n      ],\n      \"date_times\": [\n        {\n          \"date_time_type\": \"CSD\",\n          \"date_time_value\": {\n            \"seconds\": 1475136000\n          }\n        }\n      ],\n      \"notes\": [\n        {\n          \"note_type\": \"INT\",\n          \"note_value\": \"Acknowledge on order received.\"\n        }\n      ],\n      \"quantities\": [\n        {\n          \"quantity_type\": \"COR_QT\",\n          \"quantity_value\": 1234567890.1,\n          \"unit_of_measure\": \"EA\"\n        }\n      ],\n      \"change_code\": \"NOCHANGE\"\n    }\n  ]\n}",
    "timestamp" : timestamp_str
}

item_2 = {
    "_id" : timestamp_str + "002",
    "text_input": "ISA*00*          *00*          *01*197819683      *01*00060902413TST *240919*0650*U*00401*000000133*0*T*|~\nGS*PR*197819683*0060902411A2B*240919*0650*000000131*X*004010~\nST*855*600000484~\nBAK*06*AD*100002*20160923~\nREF*YB*0~\nN9*L1**Notes ~\nMSG*Acknowledge on order received.~\nPO1*1*2222.2*EA***BP*86100000~\nPID*F****Test Product 100002~\nACK*IA*2222.2*EA*069*20160930~\nN9*L1**Letters or Notes~\nMSG*Acknowledge on order received.~\nCTT*1~\nSE*12*600000484~\nGE*1*000000133~\nIEA*1*000000133~",
    "output": "{\n  \"purchase_order_header\": {\n    \"order_id\": \"100002\",\n    \"order_revision\": \"0\",\n    \"change_code\": \"NOCHANGE\",\n    \"purpose_code\": \"ACK\",\n    \"purchasing_operating_unit\": {\n      \"operating_unit_id\": \"1A2B\"\n    },\n    \"date_times\": [\n      {\n        \"date_time_type\": \"POD\",\n        \"date_time_value\": {\n          \"seconds\": 1474617600\n        }\n      }\n    ],\n    \"notes\": [\n      {\n        \"note_type\": \"INT\",\n        \"note_value\": \"Acknowledge on order received.\"\n      }\n    ]\n  },\n  \"purchase_order_lines\": [\n    {\n      \"line_id\": \"1\",\n      \"item_details\": [\n        {\n          \"item_type\": \"BITM\",\n          \"item_name\": \"86100000\",\n          \"item_description\": \"Test Product 100002\"\n        }\n      ],\n      \"date_times\": [\n        {\n          \"date_time_type\": \"CSD\",\n          \"date_time_value\": {\n            \"seconds\": 1475222400\n          }\n        }\n      ],\n      \"notes\": [\n        {\n          \"note_type\": \"INT\",\n          \"note_value\": \"Acknowledge on order received.\"\n        }\n      ],\n      \"quantities\": [\n        {\n          \"quantity_type\": \"COR_QT\",\n          \"quantity_value\": 2222.2,\n          \"unit_of_measure\": \"EA\"\n        }\n      ],\n      \"change_code\": \"NOCHANGE\"\n    }\n  ]\n}",
    "timestamp" : timestamp_str
}

item_3 = {
    "_id" : timestamp_str + "003",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240913*1137*U*00401*000000586*0*T*|~\nGS*PR*093120871T*06090241322*20240913*1137*586*X*004010~\nST*855*0001~\nBAK*06*AD*4301527920*20240905~\nPO1*10*1*EA*0.0**BP*07000503~\nPID*F****RES, 10.0 ohms, +/-1%, 0.1W, 0603, RoHS~\nACK*IA*1*EA*069*20240905**BP*07000503~\nCTT*1~\nSE*7*0001~\nGE*1*586~\nIEA*1*000000586~",
    "output": "{\n  \"purchase_order_header\": {\n    \"order_id\": \"4301527920\",\n    \"order_revision\": \"\",\n    \"change_code\": \"NOCHANGE\",\n    \"purpose_code\": \"ACK\",\n    \"purchasing_operating_unit\": {\n      \"operating_unit_id\": 22\n    },\n    \"date_times\": [\n      {\n        \"date_time_type\": \"POD\",\n        \"date_time_value\": {\n          \"seconds\": 1725523200\n        }\n      }\n    ]\n  },\n  \"purchase_order_lines\": [\n    {\n      \"line_id\": \"10\",\n      \"item_details\": [\n        {\n          \"item_type\": \"BITM\",\n          \"item_name\": \"07000503\",\n          \"item_description\": \"RES, 10.0 ohms, +/-1%, 0.1W, 0603, RoHS\"\n        }\n      ],\n      \"date_times\": [\n        {\n          \"date_time_type\": \"CSD\",\n          \"date_time_value\": {\n            \"seconds\": 1725523200\n          }\n        }\n      ],\n      \"quantities\": [\n        {\n          \"quantity_type\": \"COR_QT\",\n          \"quantity_value\": 1,\n          \"unit_of_measure\": \"EA\"\n        }\n      ],\n      \"change_code\": \"NOCHANGE\"\n    }\n  ]\n}",
    "timestamp" : timestamp_str
}

item_4 = {
    "_id" : timestamp_str + "004",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240913*1137*U*00401*000000589*0*T*|~GS*PR*093120871T*06090241322*20240913*1137*589*X*004010~ST*855*0001~BAK*06*AD*4301529060*20240910~REF*YB*0~PO1*10*1*EA*53.75**BP*1107196-01~PID*F****Memory, 16GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, 5x8, A-Die, 288-pin 1~ACK*IA*1*EA*069*20240910**BP*1107196-01~CTT*1~SE*8*0001~GE*1*589~IEA*1*000000589~",
    "output": "{\"purchase_order_header\":{\"order_id\":\"4301529060\",\"order_revision\":\"0\",\"change_code\":\"NOCHANGE\",\"purpose_code\":\"ACK\",\"purchasing_operating_unit\":{\"operating_unit_id\":22},\"date_times\":[{\"date_time_type\":\"POD\",\"date_time_value\":{\"seconds\":1725955200}}]},\"purchase_order_lines\":[{\"line_id\":\"10\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"1107196-01\",\"item_description\":\"Memory, 16GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, 5x8, A-Die, 288-pin 1\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1725955200}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":1,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"}]}",
    "timestamp" : timestamp_str
}

item_5 = {
    "_id" : timestamp_str + "005",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240913*1137*U*00401*000000585*0*T*|~GS*PR*093120871T*06090241322*20240913*1137*585*X*004010~ST*855*0001~BAK*06*AD*4301527800*20240904~PO1*10*1*EA*0.0**BP*07000503~PID*F****RES, 10.0 ohms, +/-1%, 0.1W, 0603, RoHS~ACK*IA*1*EA*069*20240904**BP*07000503~CTT*1~SE*7*0001~GE*1*585~IEA*1*000000585~",
    "output": "{\"purchase_order_header\":{\"order_id\":\"4301527800\",\"order_revision\":\"\",\"change_code\":\"NOCHANGE\",\"purpose_code\":\"ACK\",\"purchasing_operating_unit\":{\"operating_unit_id\":22},\"date_times\":[{\"date_time_type\":\"POD\",\"date_time_value\":{\"seconds\":1725436800}}]},\"purchase_order_lines\":[{\"line_id\":\"10\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"07000503\",\"item_description\":\"RES, 10.0 ohms, +/-1%, 0.1W, 0603, RoHS\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1725436800}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":1,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"}]}",
    "timestamp" : timestamp_str
}

item_6 = {
    "_id" : timestamp_str + "006",
    "text_input": "ISA*00*          *00*          *12*8652183460     *01*00060902413TST *240917*1956*U*00401*000000073*1*T*|~GS*PR*8652183460*0609024133751*20240917*195623*0073*X*004010~ST*855*0001~BAK*06*AD*4301846085*20240904~REF*YB*0~PO1*10*150000*EA**0.15000*BP*1064332-01*VP*10011591~PID*F****Microduct, For Cables, 18/14mm, 0.070in Thk x 0.535in I.D. x 0.709in O.D., HDPE,~ACK*IA*150000*EA*069*20240927~PO1*20*30000*EA**0.22000*BP*07051644*VP*10004437~PID*F****Conduit, 1.00in Dia, Smooth Wall, SDR 13.5 w/ 1250lb Pull Tape, HDPE, No Lube, O~ACK*IA*30000*EA*069*20240927~CTT*2~SE*11*0001~GE*1*0073~IEA*1*000000073~",
    "output": "{\"purchase_order_header\":{\"order_id\":\"4301846085\",\"order_revision\":\"0\",\"change_code\":\"NOCHANGE\",\"purpose_code\":\"ACK\",\"purchasing_operating_unit\":{\"operating_unit_id\":3751},\"date_times\":[{\"date_time_type\":\"POD\",\"date_time_value\":{\"seconds\":1725436800}}]},\"purchase_order_lines\":[{\"line_id\":\"10\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"1064332-01\",\"item_description\":\"Microduct, For Cables, 18/14mm, 0.070in Thk x 0.535in I.D. x 0.709in O.D., HDPE,\"},{\"item_type\":\"VITM\",\"item_name\":\"10011591\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1727424000}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":150000,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"},{\"line_id\":\"20\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"07051644\",\"item_description\":\"Conduit, 1.00in Dia, Smooth Wall, SDR 13.5 w/ 1250lb Pull Tape, HDPE, No Lube, O\"},{\"item_type\":\"VITM\",\"item_name\":\"10004437\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1727424000}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":30000,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"}]}",
    "timestamp" : timestamp_str
}

item_7 = {
    "_id" : timestamp_str + "007",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240913*1137*U*00401*000000587*0*T*|~\nGS*PR*093120871T*06090241322*20240913*1137*587*X*004010~\nST*855*0001~\nBAK*06*AD*4301528069*20240913~\nPO1*10*20*EA*0.0**BP*07123909~\nPID*F****IND, 0.45uH, 20%, DCR0.72mohm, Irms53.0A, 10.0x11.3x10.0mm, RoHS~\nACK*IA*20*EA*069*20240920**BP*07123909~\nCTT*1~\nSE*7*0001~\nGE*1*587~\nIEA*1*000000587~",
    "output": "{\n  \"purchase_order_header\": {\n    \"order_id\": \"4301528069\",\n    \"order_revision\": \"\",\n    \"change_code\": \"NOCHANGE\",\n    \"purpose_code\": \"ACK\",\n    \"purchasing_operating_unit\": {\n      \"operating_unit_id\": 22\n    },\n    \"date_times\": [\n      {\n        \"date_time_type\": \"POD\",\n        \"date_time_value\": {\n          \"seconds\": 1726214400\n        }\n      }\n    ]\n  },\n  \"purchase_order_lines\": [\n    {\n      \"line_id\": \"10\",\n      \"item_details\": [\n        {\n          \"item_type\": \"BITM\",\n          \"item_name\": \"07123909\",\n          \"item_description\": \"IND, 0.45uH, 20%, DCR0.72mohm, Irms53.0A, 10.0x11.3x10.0mm, RoHS\"\n        }\n      ],\n      \"date_times\": [\n        {\n          \"date_time_type\": \"CSD\",\n          \"date_time_value\": {\n            \"seconds\": 1726819200\n          }\n        }\n      ],\n      \"quantities\": [\n        {\n          \"quantity_type\": \"COR_QT\",\n          \"quantity_value\": 20,\n          \"unit_of_measure\": \"EA\"\n        }\n      ],\n      \"change_code\": \"NOCHANGE\"\n    }\n  ]\n}",
    "timestamp" : timestamp_str
}

item_8 = {
    "_id" : timestamp_str + "008",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240913*1137*U*00401*000000589*0*T*|~GS*PR*093120871T*06090241322*20240913*1137*589*X*004010~ST*855*0001~BAK*06*AD*4301529060*20240910~REF*YB*0~PO1*10*1*EA*53.75**BP*1107196-01~PID*F****Memory, 16GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, 5x8, A-Die, 288-pin 1~ACK*IA*1*EA*069*20240910**BP*1107196-01~CTT*1~SE*8*0001~GE*1*589~IEA*1*000000589~",
    "output": "{\"purchase_order_header\":{\"order_id\":\"4301529060\",\"order_revision\":\"0\",\"change_code\":\"NOCHANGE\",\"purpose_code\":\"ACK\",\"purchasing_operating_unit\":{\"operating_unit_id\":22},\"date_times\":[{\"date_time_type\":\"POD\",\"date_time_value\":{\"seconds\":1725955200}}]},\"purchase_order_lines\":[{\"line_id\":\"10\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"1107196-01\",\"item_description\":\"Memory, 16GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, 5x8, A-Die, 288-pin 1\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1725955200}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":1,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"}]}",
    "timestamp" : timestamp_str
}

item_9 = {
    "_id" : timestamp_str + "009",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240913*1137*U*00401*000000585*0*T*|~GS*PR*093120871T*06090241322*20240913*1137*585*X*004010~ST*855*0001~BAK*06*AD*4301527800*20240904~PO1*10*1*EA*0.0**BP*07000503~PID*F****RES, 10.0 ohms, +/-1%, 0.1W, 0603, RoHS~ACK*IA*1*EA*069*20240904**BP*07000503~CTT*1~SE*7*0001~GE*1*585~IEA*1*000000585~",
    "output": "{\"purchase_order_header\":{\"order_id\":\"4301527800\",\"order_revision\":\"\",\"change_code\":\"NOCHANGE\",\"purpose_code\":\"ACK\",\"purchasing_operating_unit\":{\"operating_unit_id\":22},\"date_times\":[{\"date_time_type\":\"POD\",\"date_time_value\":{\"seconds\":1725436800}}]},\"purchase_order_lines\":[{\"line_id\":\"10\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"07000503\",\"item_description\":\"RES, 10.0 ohms, +/-1%, 0.1W, 0603, RoHS\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1725436800}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":1,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"}]}",
    "timestamp" : timestamp_str
}

item_10 = {
    "_id" : timestamp_str + "010",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240918*0617*U*00401*000000611*0*T*|~GS*PR*093120871T*06090241322*20240918*0617*611*X*004010~ST*855*0001~BAK*06*AD*4301512420*20240610~REF*YB*0~PO1*10*6000*EA*156.0**BP*1107204-02~PID*F****Memory, 64GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, A-die, 9x4, 288-pin 2~ACK*IA*6000*EA*069*20240921**BP*1107204-02~CTT*1~SE*8*0001~GE*1*611~IEA*1*000000611~",
    "output": "{\"purchase_order_header\":{\"order_id\":\"4301512420\",\"order_revision\":\"0\",\"change_code\":\"NOCHANGE\",\"purpose_code\":\"ACK\",\"purchasing_operating_unit\":{\"operating_unit_id\":22},\"date_times\":[{\"date_time_type\":\"POD\",\"date_time_value\":{\"seconds\":1718006400}}]},\"purchase_order_lines\":[{\"line_id\":\"10\",\"item_details\":[{\"item_type\":\"BITM\",\"item_name\":\"1107204-02\",\"item_description\":\"Memory, 64GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, A-die, 9x4, 288-pin 2\"}],\"date_times\":[{\"date_time_type\":\"CSD\",\"date_time_value\":{\"seconds\":1726905600}}],\"quantities\":[{\"quantity_type\":\"COR_QT\",\"quantity_value\":6000,\"unit_of_measure\":\"EA\"}],\"change_code\":\"NOCHANGE\"}]}",
    "timestamp" : timestamp_str
}

item_11 = {
    "_id" : timestamp_str + "011",
    "text_input": "ISA*00*          *00*          *ZZ*093120871T     *01*00060902413TST *240918*0415*U*00401*000000607*0*T*|~\nGS*PR*093120871T*06090241322*20240918*0415*607*X*004010~\nST*855*0001~\nBAK*06*AD*4301512372*20240610~\nREF*YB*0~\nPO1*10*3205*EA*156.0**BP*1107204-02~\nPID*F****Memory, 64GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, A-die, 9x4, 288-pin 2~\nACK*IA*3205*EA*069*20240812**BP*1107204-02~\nPO1*20*201882*EA*156.87**BP*1106920-02~\nPID*F****Memory, 64GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, 10x4, A-Die, 288-pin~\nACK*IA*201882*EA*069*20240902**BP*1106920-02~\nCTT*2~\nSE*11*0001~\nGE*1*607~\nIEA*1*000000607~",
    "output": "{\n  \"purchase_order_header\": {\n    \"order_id\": \"4301512372\",\n    \"order_revision\": \"0\",\n    \"change_code\": \"NOCHANGE\",\n    \"purpose_code\": \"ACK\",\n    \"purchasing_operating_unit\": {\n      \"operating_unit_id\": 22\n    },\n    \"date_times\": [\n      {\n        \"date_time_type\": \"POD\",\n        \"date_time_value\": {\n          \"seconds\": 1718006400\n        }\n      }\n    ]\n  },\n  \"purchase_order_lines\": [\n    {\n      \"line_id\": \"10\",\n      \"item_details\": [\n        {\n          \"item_type\": \"BITM\",\n          \"item_name\": \"1107204-02\",\n          \"item_description\": \"Memory, 64GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, A-die, 9x4, 288-pin 2\"\n        }\n      ],\n      \"date_times\": [\n        {\n          \"date_time_type\": \"CSD\",\n          \"date_time_value\": {\n            \"seconds\": 1723449600\n          }\n        }\n      ],\n      \"quantities\": [\n        {\n          \"quantity_type\": \"COR_QT\",\n          \"quantity_value\": 3205,\n          \"unit_of_measure\": \"EA\"\n        }\n      ],\n      \"change_code\": \"NOCHANGE\"\n    },\n    {\n      \"line_id\": \"20\",\n      \"item_details\": [\n        {\n          \"item_type\": \"BITM\",\n          \"item_name\": \"1106920-02\",\n          \"item_description\": \"Memory, 64GB, Micron-Renesas-MPS, DDR5, 4800Mhz, PC5-4800, 10x4, A-Die, 288-pin\"\n        }\n      ],\n      \"date_times\": [\n        {\n          \"date_time_type\": \"CSD\",\n          \"date_time_value\": {\n            \"seconds\": 1725264000\n          }\n        }\n      ],\n      \"quantities\": [\n        {\n          \"quantity_type\": \"COR_QT\",\n          \"quantity_value\": 201882,\n          \"unit_of_measure\": \"EA\"\n        }\n      ],\n      \"change_code\": \"NOCHANGE\"\n    }\n  ]\n}",
    "timestamp" : timestamp_str
}

item_12 = {
    "_id" : timestamp_str + "012",
    "text_input": "asdfg",
    "output": "Invalid EDI Message",
    "timestamp" : timestamp_str
}

item_13 = {
    "_id" : timestamp_str + "013",
    "text_input": "ljljlllljk",
    "output": "Invalid EDI Message",
    "timestamp" : timestamp_str
}

timestamp_collection.insert_one(timestamp_1)
data_collection.insert_many([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12, item_13])

def get_validation_data(po_number):
    validation_data_collection = edi855_json_db["validation"]
    data = validation_data_collection.find({"ponumber" : po_number})
    data_string = ''
    for row in data:
        data_string = data_string + "ponumber - " + row.get("ponumber") + '\n'
        data_string = data_string + "status - " + row.get("status") + '\n'
        data_string = data_string + "podate - " + row.get("podate") + '\n'
        data_string = data_string + "lineitems - " + str(list(row.get("lineitems"))) + '\n'
    return data_string

def get_training_data():
    timestamps = edi855_json_db["timestamp"].find().sort({"timestamp":-1})
    for timestamp in timestamps:
        data = edi855_json_db["edi855_edi_json_data"].find({"timestamp" : timestamp.get("timestamp")})
        return data
    return []
