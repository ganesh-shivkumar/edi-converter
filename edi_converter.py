import google.generativeai as genai
from load_creds import load_creds
from finetune_script import finetune_model

creds = load_creds()
tunedModelName = finetune_model()
genai.configure(credentials=creds)

model = genai.GenerativeModel(model_name=tunedModelName)
response = model.generate_content("ISA*00*          *00*          *01*197819683      *01*00060902413TST *240919*0650*U*00401*000001133*0*T*|~\n GS*PR*197819683*0060902411A2B*240919*0650*000000131*X*004010~\n ST*855*600001482~\n BAK*06*AD*100222*20160922~\n REF*YB*0~\n N9*L1**Notes ~\n MSG*Acknowledge on order received.~\n PO1*1*1999.1*EA***BP*86100000~\n PID*F****Test Product 100001~\n ACK*IA*1999.1*EA*069*20160929~\n N9*L1**Letters or Notes~\n MSG*Acknowledge on order received.~\nCTT*1~\n SE*12*600001482~\n GE*1*000001133~\n IEA*1*0000001133~")
print(response.text)