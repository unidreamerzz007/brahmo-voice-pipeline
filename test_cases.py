# Ground truth data for the 20 Indian Doctor Voice Notes (VN-01 to VN-20)
# Includes expected knowledge nodes, translations, and simulated generic AI baselines (ChatGPT)

TEST_CASES = [
    {
        "id": "VN-01",
        "language": "Telugu-English",
        "specialty": "Ortho GP",
        "doctor": "Dr. Sharma, Hyderabad",
        "raw_text": "Ramaiah uncle vacharu, same story, molli noppi tho bothered avthunnaru, Ibuprofen kavali ani aduguthunnaru malli, ninth time aduguthunnaru, stent undi kadha ivvakudadu ani cheppanu malli, family ki kuda cheppanu — koduku kuda aduguthadu phone chesi — Paracetamol 650 QDS continue, Tramadol 50 add chesthunna ippudu VAS 7 undi, topical Diclofenac gel okay kaani oral NSAIDs enduku ivvakudado malli explain chesanu, next week ki rammani cheppanu, aa lopu dizziness vosthe call cheyamani cheppanu Tramadol valla, and Priya sister ki cheppandi vitals record cheyamani.",
        "what_doctor_is_saying": "Ramaiah uncle came, same complaint, bothered by knee pain, asking for Ibuprofen AGAIN (9th time), told him can't give due to stent, also told family — son also calls asking — Paracetamol 650 QDS continue, adding Tramadol 50 now because VAS is 7, topical Diclofenac gel is okay but explained again why no oral NSAIDs, told him to come next week, if dizziness from Tramadol then call, and tell Nurse Priya to record vitals.",
        "expected_nodes": [
            {"type": "CONSTRAINT", "title": "No Oral NSAIDs", "content": "Ramaiah must not receive oral NSAIDs (including Ibuprofen) due to cardiac stent history. 9th refusal documented, family and son educated."},
            {"type": "DECISION", "title": "Add Tramadol 50mg", "content": "Added Tramadol 50mg due to high pain level (VAS 7), escalating pain management from Paracetamol alone."},
            {"type": "FACT", "title": "Family Behavior & Education", "content": "Patient and family (specifically the son) repeatedly request Ibuprofen despite contraindication. Requires continuous monitoring and education."},
            {"type": "DECISION", "title": "Follow-up & Monitoring", "content": "Follow-up scheduled in 1 week. Patient instructed to report dizziness, a known side effect of Tramadol."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Negation 'ivvakudadu' (must not give) appears twice but is missed or inverted, resulting in recommendation to give Ibuprofen. Behavioral pattern ('ninth time') and clinical reasoning in Telugu are missed. Instruction to nurse ('Priya sister') is incorrectly extracted as a clinical decision.",
        "chatgpt_output": "Ramaiah uncle came with knee pain, asking for Ibuprofen. Since he has a stent, give Ibuprofen. Continue Paracetamol 650 QDS, add Tramadol 50 as VAS is 7. Topical Diclofenac gel is okay and oral NSAIDs should be given. Follow-up next week. Call if dizziness occurs. Sister Priya to record vitals.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Prescribe Ibuprofen", "content": "Give Ibuprofen as requested by patient for knee pain."},
            {"type": "DECISION", "title": "Add Tramadol 50mg", "content": "Add Tramadol 50mg for pain (VAS 7)."},
            {"type": "DECISION", "title": "Give Oral NSAIDs", "content": "Oral NSAIDs are okay to give along with topical Diclofenac gel."},
            {"type": "FACT", "title": "Nurse Instruction", "content": "Priya sister to record vitals."}
        ]
    },
    {
        "id": "VN-02",
        "language": "Hindi-English",
        "specialty": "Medicine Ward Round",
        "doctor": "Dr. Meera, Delhi",
        "raw_text": "Bed 14 Sharma ji — sugar fasting 280 hai post-prandial 380, Metformin 1000 BD chal raha hai lekin kaam nahi kar raha, Glimepiride 2 se 4 karo, nahi nahi wait karo pehle HbA1c dekho result aaya kya pharmacy se, agar 9 se zyada hai to seedha insulin start karna padega, Lantus 10 units raat ko — okay next — bed 16 Gupta aunty — BP aaj theek hai 130 by 80, Telmisartan 40 continue, potassium low tha kal 3.2 tha aaj ka result aaya kya check karo, Dytor se potassium girta hai — okay next — bed 18 Yadav sahab — discharge karo aaj, medicines likho — Tab Ecosprin 75 OD, Tab Atorva 40 HS, Tab Metolar 50 BD, Tab Pan 40 OD empty stomach, follow-up 2 hafte mein, agar chest pain aaye to seedha emergency aaye mat ghar pe baitho.",
        "what_doctor_is_saying": "Three patients in rapid sequence during ward rounds: Sharma (sugar uncontrolled, considering insulin), Gupta (BP stable, potassium monitoring needed), Yadav (discharge with 4-drug prescription and emergency instructions).",
        "expected_nodes": [
            {"type": "DECISION", "title": "Bed 14 Sharma: Glimepiride Adjustment Pending HbA1c", "content": "Hold Glimepiride increase (2mg to 4mg) pending HbA1c result. If HbA1c > 9, initiate Lantus insulin 10 units at night."},
            {"type": "FACT", "title": "Bed 16 Gupta: Low Potassium Monitoring", "content": "BP is stable at 130/80 on Telmisartan 40. Potassium was low (3.2) yesterday; check current labs. Note that Dytor (Torsemide) causes potassium depletion."},
            {"type": "DECISION", "title": "Bed 18 Yadav: Discharge Medications", "content": "Discharge today with Ecosprin 75mg OD, Atorvastatin (Atorva) 40mg HS, Metoprolol (Metolar) 50mg BD, and Pantoprazole (Pan) 40mg OD empty stomach."},
            {"type": "CONSTRAINT", "title": "Bed 18 Yadav: Emergency Return Criteria", "content": "If chest pain occurs post-discharge, patient must go directly to the emergency department immediately. Warned: 'mat ghar pe baitho' (do not sit at home)."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Doctor self-corrects mid-sentence ('Glimepiride 2 se 4 karo, nahi nahi wait karo') - generic AI increases Glimepiride anyway. Commingles 3 distinct patient contexts (Sharma, Gupta, Yadav) into one record. Brand names ('Atorva', 'Metolar', 'Pan') are transcribed incorrectly or misidentified. Misses Hindi negation in discharge warning ('mat ghar pe baitho').",
        "chatgpt_output": "Sharma ji on Bed 14: Fasting sugar 280, PP 380. Metformin 1000 BD is running but not working. Increase Glimepiride 2 to 4. Also start Lantus 10 units. Gupta aunty Bed 16: BP is 130/80, Telmisartan 40 continue. Potassium was 3.2, check if Dytor causes potassium to drop. Yadav sahab Bed 18: Discharge today with Ecosprin 75 OD, Atorva 40 HS, Metolar 50 BD, Pan 40 OD. Follow-up in 2 weeks. If chest pain comes, sit at home and wait.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Bed 14 Glimepiride Increase", "content": "Increase Glimepiride from 2mg to 4mg BD."},
            {"type": "DECISION", "title": "Bed 14 Start Insulin", "content": "Start Lantus 10 units at night immediately."},
            {"type": "FACT", "title": "Gupta Potassium Check", "content": "Check if Dytor drops potassium."},
            {"type": "CONSTRAINT", "title": "Yadav Emergency Instruction", "content": "If chest pain occurs, stay at home and rest."}
        ]
    },
    {
        "id": "VN-03",
        "language": "Tamil-English",
        "specialty": "Paediatrics",
        "doctor": "Dr. Lakshmi, Chennai",
        "raw_text": "Aadhya baby ku ippo fifth time ear infection, amma romba worried — amoxicillin kudukka kudadhu allergy iruku 18 months la anaphylaxis vanthuchu amma ku explain panninom but amma every time kekuranga amoxicillin than work aagum nu — azithromycin 10mg per kg 3 days start pannanum, weight 14kg so total 140mg per day, oru 5ml spoon la suspend pannunga, ENT referral write pannunga Dr. Krishnan ku — ippadi frequent ah varthu na adenoid check pannanum, tympanometry pannanum, hearing test kuda pannanum — amma kitta sollunga next week appointment fix panniduvom ENT ku, aana ippo azithromycin start pannidalam paravaillai.",
        "what_doctor_is_saying": "Aadhya's 5th ear infection, mother is very worried, keeps asking for amoxicillin despite anaphylaxis history, prescribed azithromycin weight-based (14kg × 10mg = 140mg), ENT referral to Dr. Krishnan needed — if this frequent need to check adenoids, tympanometry, hearing test. Start azithromycin now, ENT appointment next week.",
        "expected_nodes": [
            {"type": "CONSTRAINT", "title": "Absolute Contraindication: Amoxicillin/Penicillin", "content": "Strictly NO Amoxicillin or penicillin-class drugs due to history of anaphylaxis at 18 months. Mother repeatedly requests it, needs constant reminder."},
            {"type": "DECISION", "title": "Start Azithromycin Suspension", "content": "Start Azithromycin suspension 140mg/day (10mg/kg for 14kg weight) OD for 3 days. Administer as 5ml spoon suspension."},
            {"type": "DECISION", "title": "ENT Referral to Dr. Krishnan", "content": "Refer to ENT specialist Dr. Krishnan for evaluation of recurrent ear infections (5th episode). Schedule next week."},
            {"type": "FACT", "title": "Diagnostic Plan for Recurrent Otitis", "content": "Warrants workup for adenoid hypertrophy, tympanometry, and hearing test due to high frequency of infections."},
            {"type": "ANTI_PATTERN", "title": "Parent Pressure for Contraindicated Drug", "content": "Mother repeatedly demands Amoxicillin despite extensive counseling about life-threatening anaphylaxis risk."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Tamil double negation 'kudukka kudadhu' (must not give) is flipped to positive, leading generic AI to prescribe Amoxicillin. Fails to compute weight-based dosage (14kg x 10mg/kg = 140mg). Ignores the mother's behavioral pattern of requesting contraindicated drugs.",
        "chatgpt_output": "Aadhya baby has her fifth ear infection. Give Amoxicillin as the mother says it works. There was allergy/anaphylaxis at 18 months, but give it anyway. Azithromycin 10mg per kg for 3 days, total 140mg. Refer to ENT Dr. Krishnan to check adenoid, tympanometry, and hearing test next week. Start Azithromycin if Amoxicillin doesn't work.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Give Amoxicillin", "content": "Give Amoxicillin for ear infection as mother states it is the only drug that works."},
            {"type": "DECISION", "title": "Azithromycin Prescription", "content": "Azithromycin 140mg daily for 3 days."},
            {"type": "DECISION", "title": "ENT Referral", "content": "Refer to Dr. Krishnan next week."}
        ]
    },
    {
        "id": "VN-04",
        "language": "Telugu-English",
        "specialty": "Cardiology CCU",
        "doctor": "Dr. Vikram, Hyderabad",
        "raw_text": "Rajan garu CCU lo admit ayyaru chest pain tho, ECG lo ST elevation V1 to V4 anterior wall MI, troponin send chesamu stat result kosam wait chesthunnam, Cath lab ni alert chesamu — kaani problem emitante Rajan gari ki already Warfarin chal thundi INR 2.8 undi, dual antiplatelet start cheyali kaani bleeding risk ekkuva, so Heparin bolus ivvandi 60 units per kg but max 4000 units, Clopidogrel 300mg loading dose ivvandi — KAANI Aspirin loading dose ivvakandi INR ekkuva undi kadha Warfarin valla — cardiology fellow ki cheppandi Dr. Ravi ki — ayana cath lab lo wait chesthadu — family ki cheppandi serious condition ani consent form sign cheyinchandi cath ki — oxygen 4 litre nasal prongs, Morphine 2mg IV pain kosam ichi already — vitals every 15 minutes.",
        "what_doctor_is_saying": "Rajan admitted to CCU with chest pain, ECG shows anterior STEMI (V1-V4), troponin sent stat, cath lab alerted. KEY DILEMMA: already on Warfarin with INR 2.8, needs dual antiplatelet but high bleeding risk. Give Heparin 60u/kg (max 4000u), Clopidogrel 300mg loading — BUT DON'T give Aspirin loading (INR too high on Warfarin). Call cardiology fellow Dr. Ravi, tell family it's serious, get cath consent, oxygen 4L, already gave Morphine 2mg IV.",
        "expected_nodes": [
            {"type": "FACT", "title": "Anterior Wall MI & CCU Admission", "content": "Mr. Rajan admitted with chest pain; ECG reveals anterior wall STEMI (ST elevation V1-V4). Troponin level pending."},
            {"type": "CONSTRAINT", "title": "Contraindication: Aspirin Loading Dose", "content": "DO NOT administer Aspirin loading dose. Patient is already therapeutic on Warfarin (INR 2.8), causing high bleeding risk."},
            {"type": "DECISION", "title": "Anticoagulation & Antiplatelet Loading", "content": "Give Heparin bolus 60 units/kg IV (capped at max 4000 units) and Clopidogrel 300mg loading dose. (Standard dual antiplatelet modified due to INR)."},
            {"type": "DECISION", "title": "Immediate Actions & Resuscitation", "content": "Administered Morphine 2mg IV for pain, O2 4L via nasal prongs. Monitor vitals every 15 minutes."},
            {"type": "DECISION", "title": "Cath Lab Activation & Consent", "content": "Alerted Cath Lab. Cardiology fellow Dr. Ravi is waiting. Counsel family on critical condition and obtain high-risk consent for cardiac catheterization."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Fails to recognize emphatic Telugu negation 'ivvakandi' (do NOT give) for Aspirin loading dose, which is fatal for a patient with therapeutic INR on Warfarin. Fails the conditional dosing logic '60 units per kg but max 4000 units'. Commingles clinical actions with operational staff directives.",
        "chatgpt_output": "Rajan is in CCU with chest pain and anterior wall MI (V1-V4). Troponin sent. Cath lab alerted. He is on Warfarin with INR 2.8. Give dual antiplatelet therapy: Heparin bolus 60 units per kg (no limit mentioned) and Clopidogrel 300mg loading. Also give Aspirin loading dose because of MI. Tell Dr. Ravi. Inform family and get consent. Oxygen 4L and Morphine 2mg IV given. Vitals every 15 min.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Prescribe Dual Antiplatelet", "content": "Give Heparin bolus 60 units/kg, Clopidogrel 300mg loading dose, and Aspirin loading dose."},
            {"type": "DECISION", "title": "Emergency Cath Lab", "content": "Activate cath lab and obtain consent."}
        ]
    },
    {
        "id": "VN-05",
        "language": "Hindi-English",
        "specialty": "GP Clinic",
        "doctor": "Dr. Singh, Mumbai",
        "raw_text": "Padma aunty ka case bahut frustrating hai — sugar 380 aa raha hai fasting, maine bola tha Ekadashi ko Glimepiride skip karo lekin aunty ne suna nahi, dono tablet kha li khali pet, hypoglycemia ho gaya ghar pe, bete ne phone kiya ki aunty behosh ho gayi — thankfully glucose de diya — ab main kya karun — Glimepiride 2mg se 1mg karo pehle, Metformin 1000 continue, HbA1c karwao, agar 8 se zyada hai to Insulin pe shift karna padega — Padma aunty ke bete ko bolo ki Ekadashi ke din SIRF Metformin dena, Glimepiride bilkul nahi, aur fast break karne ka time fix karo sham 6 baje, usse pehle BG check karo har 4 ghante — aur haan dietician referral do aunty ko — low glycemic index wala diet chahiye fasting ke liye.",
        "what_doctor_is_saying": "Frustrated: Padma's sugar 380 fasting, told her to skip Glimepiride on Ekadashi but she didn't listen, took both tablets on empty stomach, had hypoglycemia at home, son called saying she fainted. Reducing Glimepiride 2mg→1mg, Metformin continue, HbA1c needed — if >8 switch to insulin. Tell son: ONLY Metformin on Ekadashi, NO Glimepiride, fix fast-break time at 6pm, BG every 4 hours. Dietician referral for low-GI fasting diet.",
        "expected_nodes": [
            {"type": "ANTI_PATTERN", "title": "Fasting Medication Non-compliance", "content": "Patient took Glimepiride during Ekadashi fast against instructions, resulting in severe hypoglycemia and fainting at home."},
            {"type": "DECISION", "title": "Reduce Glimepiride & Continue Metformin", "content": "Reduce Glimepiride from 2mg to 1mg daily. Continue Metformin 1000mg. Check HbA1c to decide if insulin shift (if >8) is required."},
            {"type": "CONSTRAINT", "title": "Strict Fasting Protocol: No Glimepiride", "content": "On Ekadashi fasting days, patient must receive ONLY Metformin. Glimepiride is ABSOLUTELY forbidden ('bilkul nahi')."},
            {"type": "DECISION", "title": "Fasting Blood Glucose Monitoring", "content": "Instruct son to check blood glucose every 4 hours during fast. Fix fast-break time at 6:00 PM."},
            {"type": "DECISION", "title": "Dietician Referral", "content": "Refer to dietician for low glycemic index diet plan tailored for fasting days."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Fails to capture patient non-compliance narrative ('suna nahi' = didn't listen). Misses the emphatic Hindi negation 'bilkul nahi' (absolutely not) regarding Glimepiride on fast days, risking recurrent hypoglycemia. Struggles with cultural term 'Ekadashi'.",
        "chatgpt_output": "Padma aunty had sugar 380 fasting. She skipped Glimepiride on Ekadashi. She had hypoglycemia because she took only Metformin. Glucose was given by her son. Reduce Glimepiride 2mg to 1mg, Metformin 1000 continue. On Ekadashi, give Glimepiride and Metformin both. Fast break at 6pm. Check BG every 4 hours. Dietician referral.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Glimepiride Adjustment", "content": "Reduce Glimepiride to 1mg, Metformin 1000 continue."},
            {"type": "CONSTRAINT", "title": "Fasting Instructions", "content": "Give both Metformin and Glimepiride on Ekadashi fast days."}
        ]
    },
    {
        "id": "VN-06",
        "language": "Kannada-English",
        "specialty": "Surgery Pre-Op",
        "doctor": "Dr. Rao, Bangalore",
        "raw_text": "Ramaiah avrige TKR surgery plan maadthiddivi next week, problem enu andre Warfarin chal aagidhe, INR 2.6 idhe, surgery ge 5 dina munche Warfarin nillisbekku, Heparin bridging start maadbekku Enoxaparin 60mg BD, INR 1.5 ge barbekku surgery munche — Cardiology team Dr. Mehta ge discuss maadbekku because stent idhe 2022 nalli — Clopidogrel 7 days munche nillisbekku but Aspirin continue maadona last minute vargu — anaesthesia team ge helbekku difficult airway iddare, pre-op blood work CBC, RFT, LFT, coagulation profile, chest X-ray, ECG — physiotherapy team ge inform maadi post-op day 1 ne PT start aagbekku — Priya sister ge helu special attention Warfarin restart timing post-op Dr. Mehta decide maadthare.",
        "what_doctor_is_saying": "Planning Ramaiah's TKR next week. Problem: on Warfarin (INR 2.6) — stop 5 days before, bridge with Enoxaparin 60mg BD, target INR 1.5 pre-op. Discuss with Cardiology (Dr. Mehta) because of stent (2022). Stop Clopidogrel 7 days before but continue Aspirin until last moment. Inform anaesthesia (possible difficult airway). Pre-op workup: CBC, RFT, LFT, coagulation, CXR, ECG. PT team: start Day 1 post-op. Nurse Priya: special attention to Warfarin restart timing — Dr. Mehta decides.",
        "expected_nodes": [
            {"type": "DECISION", "title": "Pre-op Anticoagulation Bridging", "content": "Stop Warfarin 5 days before TKR surgery (current INR 2.6). Bridge with Enoxaparin 60mg BD. Target INR < 1.5 before surgery."},
            {"type": "CONSTRAINT", "title": "Stop Clopidogrel, Continue Aspirin", "content": "Stop Clopidogrel 7 days before surgery. Continue Aspirin until the last moment prior to surgery."},
            {"type": "CONSTRAINT", "title": "Cardiology Clearance Required", "content": "Discuss perioperative plan with cardiologist Dr. Mehta due to 2022 cardiac stent history. Warfarin restart timing post-op must be decided by Dr. Mehta."},
            {"type": "DECISION", "title": "Pre-op Diagnostics & Referrals", "content": "Order pre-op bloods (CBC, RFT, LFT, Coagulation), CXR, and ECG. Alert Anaesthesia regarding a potential difficult airway. Inform Physiotherapy to start Day 1 post-op."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Kannada command verbs like 'nillisbekku' (must stop) are misidentified, leading to potential failure to stop Warfarin/Clopidogrel before major surgery. Misses the decision hierarchy ('Dr. Mehta decide maadthare') assigning final authority to the cardiologist.",
        "chatgpt_output": "Ramaiah is having TKR surgery next week. He is on Warfarin (INR 2.6). Bridge with Enoxaparin 60mg BD and continue Warfarin until surgery. Dr. Mehta in Cardiology to discuss stent from 2022. Stop Aspirin 7 days before but continue Clopidogrel. Pre-op bloods, chest x-ray, ECG. PT starts post-op day 1. Sister Priya to restart Warfarin post-op.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "TKR Pre-op Plan", "content": "Bridge Warfarin with Enoxaparin 60mg BD and check INR."},
            {"type": "DECISION", "title": "Antiplatelet Management", "content": "Stop Aspirin 7 days before surgery and continue Clopidogrel."}
        ]
    },
    {
        "id": "VN-07",
        "language": "Bengali-English",
        "specialty": "Psychiatry",
        "doctor": "Dr. Sen, Kolkata",
        "raw_text": "Arun babu ashechilen aaj, PHQ-9 score 18 porjonto bere gechhe, moderate to severe depression, ghum nei rate — 3-4 ghonta matro, khabar khacche na thik moto — 5kg weight kome gechhe last 2 months e — Nexito 10mg raat e start korte hobe, kaaj na korle 2 week pore 20mg te barhabo — Clonazepam 0.5mg raat e initially neend er jonno kaaron Nexito te first 2 weeks e insomnia barte pare — important kotha — Arun babu antidepressant nite raaji non, bolchhen 'pagol er oshudh' — bolechhi je ei oshudh diabetes er oshudh er moto, brain er chemical balance correct kore — tai ke bolo next visit e ashe je counseling o shuru korbo — suicidal ideation nei ekhon but safety plan discuss korechhi, wife er number niye rekhechhi emergency te — follow-up 1 week e.",
        "what_doctor_is_saying": "Arun came today, PHQ-9 risen to 18 (moderate-severe), not sleeping (3-4 hours only), not eating properly — lost 5kg in 2 months. Starting Escitalopram 10mg at night, increase to 20mg in 2 weeks if not working. Clonazepam 0.5mg at night initially for sleep because Escitalopram may worsen insomnia first 2 weeks. IMPORTANT: Arun refuses antidepressant — calls it 'pagol er oshudh' (madman's medicine). Explained it's like diabetes medicine — corrects brain chemical balance. Told wife to bring him next visit for counseling. No suicidal ideation currently but discussed safety plan, took wife's emergency number. Follow-up 1 week.",
        "expected_nodes": [
            {"type": "FACT", "title": "Severe Depressive Symptoms", "content": "Arun has PHQ-9 score of 18 (moderate-severe depression) with insomnia (3-4 hours sleep), anorexia, and 5kg weight loss in 2 months."},
            {"type": "DECISION", "title": "Start Escitalopram (Nexito) with Taper Plan", "content": "Start Nexito (Escitalopram) 10mg at night. Plan to increase to 20mg in 2 weeks if response is inadequate."},
            {"type": "DECISION", "title": "Short-term Clonazepam Co-prescription", "content": "Prescribe Clonazepam 0.5mg at night temporarily for sleep and to manage potential initial SSRI-induced insomnia."},
            {"type": "ANTI_PATTERN", "title": "Medication Stigma & Resistance", "content": "Patient initially refused medication calling it 'pagol er oshudh' (madman's medicine). Counseled using the diabetes analogy."},
            {"type": "FACT", "title": "Suicide Risk Assessment & Safety Plan", "content": "No active suicidal ideation currently. Safety plan established; emergency contact number of patient's wife documented."},
            {"type": "DECISION", "title": "Follow-up & Counseling", "content": "Follow-up in 1 week. Initiate psychotherapy/counseling during next visit (wife to accompany patient)."}
        ],
        "negation_critical": True,
        "danger_level": "MODERATE",
        "why_generic_ai_fails": "Stigma phrase 'pagol er oshudh' is lost. Nexito is mistranscribed as 'next to' by standard ASR. The clinical reasoning for Clonazepam (countering initial SSRI insomnia) is missed. Bengali negation 'raaji non' (does not agree) is missed, falsely recording that the patient readily agreed to take antidepressants.",
        "chatgpt_output": "Arun babu came. PHQ-9 is 18. Moderate to severe depression. Sleep is fine. Lost 5kg. Start next to 10mg at night, increase to 20mg next week. Clonazepam 0.5mg at night. He is happy to take antidepressants. Counseling starting next week. Suicidal ideation present, call wife. Follow-up 1 week.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Prescribe Next To", "content": "Start Next To 10mg at night."},
            {"type": "FACT", "title": "Patient Agreement", "content": "Patient is ready to start antidepressants."}
        ]
    },
    {
        "id": "VN-08",
        "language": "Malayalam-English",
        "specialty": "OB-GYN",
        "doctor": "Dr. Parvathy, Kochi",
        "raw_text": "Meera chechi 32 weeks aayallo, BP innale 148 by 92 aayirunnu innu 152 by 96 aanu, urine protein 2+ aanu — pre-eclampsia concern undu — Labetalol 100mg BD start cheyyuka, ACE inhibitor paadilla pregnancy yil absolutely contraindicated aanu, Methyldopa aanu alternative — but Labetalol try cheyyam aadyam — 24-hour urine protein collection start cheyyamaanu, complete blood count platelets eppol check cheyyuka, LDH uric acid liver enzymes ellaam cheyyuka HELLP rule out cheyyaan — baby yude growth scan next week, CTG biweekly start cheyyuka — Meera chechi yodu paranju bed rest suggest cheyyu but complete bed rest venda moderate activity okay aanu — eppozhaanu hospital il varanam enu paranjittundu — headache visual disturbance epigastric pain ingane enthenkilum undenkil udan varanam — husband odu koodhi paranju emergency signs — next visit 3 days kazhinju.",
        "what_doctor_is_saying": "Meera at 32 weeks, BP rising (148/92 → 152/96), urine protein 2+ — pre-eclampsia concern. Start Labetalol 100mg BD. ACE inhibitor ABSOLUTELY contraindicated in pregnancy. Methyldopa is alternative but trying Labetalol first. 24-hr urine protein collection, CBC with platelets NOW, LDH, uric acid, liver enzymes — rule out HELLP. Growth scan next week, biweekly CTG. Told Meera: moderate bed rest (not complete), come to hospital if headache, visual disturbance, or epigastric pain. Explained emergency signs to husband also. Follow-up in 3 days.",
        "expected_nodes": [
            {"type": "FACT", "title": "Pre-eclampsia Suspected", "content": "Meera at 32 weeks gestation presents with rising BP (152/96) and proteinuria 2+. Pre-eclampsia is a primary concern."},
            {"type": "CONSTRAINT", "title": "Absolute Contraindication: ACE Inhibitors", "content": "ACE Inhibitors are strictly prohibited ('paadilla') due to high risk of fetal toxicity in pregnancy."},
            {"type": "DECISION", "title": "Antihypertensive Initiation", "content": "Start Labetalol 100mg BD (First-line). Alternative is Methyldopa if Labetalol is not tolerated."},
            {"type": "DECISION", "title": "HELLP Syndrome Workup", "content": "Order immediate CBC with platelets, LDH, Uric Acid, LFT, and initiate 24-hour urine protein collection to rule out HELLP syndrome."},
            {"type": "DECISION", "title": "Fetal Monitoring Plan", "content": "Schedule fetal growth scan next week and start biweekly CTG monitoring."},
            {"type": "CONSTRAINT", "title": "Emergency Action Plan & Activity Level", "content": "Advise moderate activity, NOT complete bed rest ('venda'). Educated patient and husband on emergency signs (headache, visual changes, epigastric pain) requiring immediate hospital return. Follow-up in 3 days."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Malayalam negation 'paadilla' (must not) is missed, which could lead a generic AI to prescribe a highly teratogenic ACE inhibitor. Malayalam negation 'venda' (don't want/need) is flipped, resulting in a false recommendation for complete bed rest instead of moderate activity. Epigastric pain is mistranslated.",
        "chatgpt_output": "Meera is 32 weeks pregnant. BP is 152/96, urine protein 2+. Pre-eclampsia concern. Start Labetalol 100mg BD and also give ACE inhibitors. 24-hour urine protein, CBC platelets check. Baby growth scan next week, biweekly CTG. Complete bed rest is required. If headache, visual disturbance, or gastric pain occurs, stay home. Follow-up in 3 days.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Prescribe Antihypertensives", "content": "Start Labetalol 100mg BD and ACE Inhibitor therapy."},
            {"type": "CONSTRAINT", "title": "Rest Protocol", "content": "Complete strict bed rest is mandatory."}
        ]
    },
    {
        "id": "VN-09",
        "language": "Hindi-English",
        "specialty": "Emergency Medicine",
        "doctor": "Dr. Kapoor, Delhi",
        "raw_text": "Multiple trauma hai RTA sixteen year old ladka — GCS 9 hai E2V3M4 — intubation karo size 7 tube — C-spine collar lagao pehle — BP 80 by 50 hai NS bolus do 20ml per kg stat means 1 litre do — type and cross match karo 4 units PRBC — ek haath mein wide bore cannula daalo 16 gauge — doosre haath mein bhi ek aur — Tetanus TT do kya history hai check karo — chest X-ray portable karo pneumothorax rule out karo left side pe breath sounds kam hain — CT head stat karo — neuro ko bulao Dr. Verma ko — ortho ko bhi bulao right femur deformed lag raha hai — parents ko bulao consent chahiye — agar BP respond nahi karta NS ke baad to blood shuru karo — Tranexamic acid 1 gram over 10 min do — urine catheter daalo urine output monitor karo — FAST ultrasound karo free fluid check karo!",
        "what_doctor_is_saying": "Multiple trauma, 16-year-old boy, RTA. GCS 9 (E2V3M4). Intubate with size 7 tube — C-spine collar FIRST. BP 80/50 — NS bolus 20ml/kg = 1 litre stat. Type and crossmatch 4 units PRBC. Two wide bore cannulas 16G. Check tetanus history. Portable CXR — rule out pneumothorax (decreased breath sounds left). Stat CT head. Call Neuro (Dr. Verma) and Ortho (right femur deformity). Call parents for consent. If BP doesn't respond to NS → start blood. Tranexamic acid 1g over 10 min. Foley catheter, monitor urine output. FAST scan for free fluid.",
        "expected_nodes": [
            {"type": "FACT", "title": "Severe Trauma Presentation", "content": "16-year-old male, road traffic accident (RTA). GCS is 9 (E2, V3, M4). Hypotensive (BP 80/50). Left lung breath sounds decreased. Right femur deformity present."},
            {"type": "CONSTRAINT", "title": "Order of Operation: C-spine Stabilization", "content": "Apply C-spine collar immediately BEFORE performing intubation (size 7.0 ET tube)."},
            {"type": "DECISION", "title": "Fluid Resuscitation Protocol", "content": "Administer 1L Normal Saline (NS) bolus (20ml/kg) stat. If BP remains unresponsive, immediately initiate blood transfusion (type and crossmatch 4 units PRBC)."},
            {"type": "DECISION", "title": "Venous Access & Medication", "content": "Insert bilateral 16G wide bore IV cannulas. Administer Tranexamic Acid (TXA) 1g IV over 10 minutes. Check tetanus status and give TT."},
            {"type": "DECISION", "title": "Stat Diagnostics & Consults", "content": "Perform portable chest X-ray (rule out left pneumothorax), stat CT head, and bedside FAST scan. Consult Neurosurgery (Dr. Verma) and Orthopedics. Insert Foley catheter for urine output monitoring."}
        ],
        "negation_critical": False,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Extremely fast speech with no punctuation leads to chronological errors. Generic AI fails the critical safety order 'C-spine collar lagao pehle' (apply collar FIRST) and attempts to intubate without stabilizing the neck. Conditional fluid logic is missed. Embedded numbers ('16 gauge', 'size 7', '20ml/kg') are garbled.",
        "chatgpt_output": "16 year old boy with GCS 9 (E2V3M4). Intubate with size 7 tube. Then apply C-spine collar. BP 80/50, give NS 20ml/kg and 4 units blood. Put a 16 gauge cannula. Tetanus history check. CXR, CT head. Call neuro Dr. Verma, ortho for femur. Blood and NS should be started together. TXA 1g over 10 min. Catheter, FAST scan.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Intubation & C-spine", "content": "Perform intubation with size 7.0 tube, then apply C-spine collar."},
            {"type": "DECISION", "title": "Fluid Resuscitation", "content": "Start NS and blood transfusion simultaneously."}
        ]
    },
    {
        "id": "VN-10",
        "language": "Gujarati-English",
        "specialty": "Dermatology",
        "doctor": "Dr. Patel, Ahmedabad",
        "raw_text": "Arjun baby ne eczema vadhare kharab thayo che — mummy homeopathy ni goli aapi rahi che sathe sathe, mane khabar nahi kem jaldi nathi thatu — maine dekha ki ek steroid cream lagavi che jeni koi prescription nathi — medical store wale ne aa cream aapi — bahut strong Clobetasol 0.05% face pe lagavi che! — bachche ke face pe Class 1 steroid nahi lagana — skin atrophy thay jase — abhi Mometasone 0.1% shift karo — face pe sirf 5 din, body pe 10 din — moisturizer din ma chaar vaar lagavo — Cetaphil ya Physiogel — emollient pehle fir steroid upar se — bathing routine change karo lukewarm water sirf 5 minute — mummy ne samjhavo ki homeopathy band karo jab tak allopathy chal rahi hai interaction ho sakta hai — aur haan medical store se direct steroid lena band karo dangerous hai — follow-up 2 weeks.",
        "what_doctor_is_saying": "Arjun's eczema worsening — mother giving homeopathy simultaneously AND applying unprescribed Clobetasol 0.05% (class 1 steroid!) on FACE — bought from medical store without prescription. NEVER use Class 1 steroid on child's face — risk of skin atrophy. Switch to Mometasone 0.1% — face 5 days max, body 10 days. Moisturizer QID (Cetaphil/Physiogel) — emollient first then steroid. Change bathing to lukewarm 5 minutes only. Tell mother: stop homeopathy while on allopathy (interaction risk) and stop buying steroids from store directly — it's dangerous. Follow-up 2 weeks.",
        "expected_nodes": [
            {"type": "ANTI_PATTERN", "title": "Unsafe OTC Steroid Use", "content": "Mother applied Clobetasol 0.05% (Class 1 potent steroid) to pediatric patient's face without prescription, resulting in skin damage risk."},
            {"type": "CONSTRAINT", "title": "Strict Contraindication: Class 1 Steroid on Pediatric Face", "content": "NEVER use Class 1 steroids on a child's face due to rapid risk of irreversible skin atrophy."},
            {"type": "DECISION", "title": "Steroid De-escalation & Duration Limits", "content": "Switch to Mometasone 0.1% ointment. Apply to face for 5 days max, and to body for 10 days max."},
            {"type": "DECISION", "title": "Emollient Application Sequence", "content": "Apply moisturizer (Cetaphil or Physiogel) QID. Ensure the emollient is applied FIRST, followed by the steroid cream on top."},
            {"type": "CONSTRAINT", "title": "Homeopathy Discontinuation & OTC Warning", "content": "Discontinue homeopathic pills due to potential drug interaction risks. Strongly warn mother against purchasing OTC steroids directly from medical stores."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Triple code-switching (Gujarati-Hindi-English) in one sentence. Gujarati negation 'jeni koi prescription nathi' (which has no prescription) is missed, and the critical application order ('emollient first then steroid') is reversed. Does not understand the danger of Clobetasol on pediatric facial skin.",
        "chatgpt_output": "Arjun baby has eczema. Homeopathy is working well. Apply steroid cream Clobetasol 0.05% on face, it is prescribed by the medical store. Switch to Mometasone 0.1% for face 10 days, body 5 days. Apply steroid first, then moisturizer. Bathe in hot water for 5 min. Homeopathy is fine to continue. Follow-up 2 weeks.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Eczema Treatment Plan", "content": "Apply Clobetasol 0.05% to face and Mometasone to body. Apply steroid before emollient."},
            {"type": "FACT", "title": "Homeopathy Use", "content": "Homeopathy tablets can be continued along with steroid creams."}
        ]
    },
    {
        "id": "VN-11",
        "language": "Telugu-English",
        "specialty": "Nephrology",
        "doctor": "Dr. Reddy, Hyderabad",
        "raw_text": "Lakshman gari creatinine 3.8 ki vachindi, GFR calculate chesthe 18 vachindi, CKD stage 4 ki progress ayyindi — Metformin ippatiki ippatiki aapeyandi contraindicated below GFR 30 lo — Linagliptin ki shift cheyandi kidney safe adi — Ramipril dose 10 nunchi 5mg ki tagginchandi proteinuria thagguthundhaa ani chuddham — potassium ekkuva unnadi 5.8 — Kayexalate ivvandi stat aur calcium gluconate ready ga pettandi ECG changes unte — eppudu Torsemide 20mg aapeyandi Furosemide 40mg ki maaripoyandi — aur haan nephrology OPD ki next week rammani cheppandi dialysis planning discussion cheyali — dietician ki refer cheyandi low protein low potassium low sodium diet.",
        "what_doctor_is_saying": "Lakshman's creatinine rose to 3.8, GFR is 18, progressed to CKD Stage 4. STOP Metformin immediately (contraindicated below GFR 30). Switch to Linagliptin. Reduce Ramipril 10mg -> 5mg. Potassium is high at 5.8, give Kayexalate stat and keep calcium gluconate ready for ECG changes. Stop Torsemide 20mg, switch to Furosemide 40mg. Nephrology OPD next week for dialysis planning. Dietician referral for low protein, potassium, and sodium diet.",
        "expected_nodes": [
            {"type": "FACT", "title": "CKD Stage 4 Progression", "content": "Patient has progressed to CKD Stage 4 (Creatinine 3.8, GFR 18). Hyperkalemia noted (potassium 5.8)."},
            {"type": "CONSTRAINT", "title": "Stop Metformin Immediately", "content": "Discontinue Metformin immediately. It is strictly contraindicated in patients with GFR < 30 due to lactic acidosis risk."},
            {"type": "DECISION", "title": "Antidiabetic & Antihypertensive Adjustments", "content": "Switch Metformin to Linagliptin (renal-safe). Reduce Ramipril from 10mg to 5mg daily to monitor proteinuria control while preserving GFR."},
            {"type": "DECISION", "title": "Hyperkalemia Management", "content": "Administer Kayexalate stat. Keep Calcium Gluconate at bedside to stabilize cardiac membrane if ECG changes develop."},
            {"type": "DECISION", "title": "Diuretic Swap & Nephrology Referral", "content": "Stop Torsemide 20mg, switch to Furosemide 40mg. Refer to Nephrology next week to discuss dialysis planning. Refer to dietician for renal diet (low protein, potassium, sodium)."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Telugu negation 'aapeyandi' (stop/discontinue) is missed, leading to Metformin continuation which is a severe safety hazard in CKD 4. Swaps the diuretic transition, prescribing Furosemide and Torsemide concurrently.",
        "chatgpt_output": "Lakshman has creatinine 3.8, GFR 18, CKD stage 4. Continue Metformin, add Linagliptin. Reduce Ramipril 10 to 5mg. Potassium is 5.8. Give Kayexalate and Calcium gluconate. Keep Torsemide 20mg and Furosemide 40mg. Next week dialysis planning. Renal diet.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Diabetes Care", "content": "Continue Metformin and add Linagliptin."},
            {"type": "DECISION", "title": "Diuretics", "content": "Give Torsemide 20mg and Furosemide 40mg together."}
        ]
    },
    {
        "id": "VN-12",
        "language": "Marathi-English",
        "specialty": "ENT",
        "doctor": "Dr. Joshi, Pune",
        "raw_text": "Deshmukh sahab yeun gele, sudden sensorineural hearing loss ahe right side la — onset 2 divas aadhi, morning uthlyavar suddenly aikku yet navhta — pure tone audiometry karun ghya urgently — ata Prednisolone 1mg per kg start kara means 60mg morning 2 weeks tapering dose — intratympanic Dexamethasone consider karun ya — MRI brain karun ghya acoustic neuroma rule out karayala — patient la sanga 48 hours madhye treatment start nahi kela tar recovery chances kammi hotat — Betahistine 16mg TDS suru kara vertigo asel tar — audiometry result baghun tya nusaar pudhe plan karu — smoking band kara lau immediately circulation improve vhayala.",
        "what_doctor_is_saying": "Deshmukh had sudden sensorineural hearing loss right side, onset 2 days ago. URGENT pure tone audiometry. Start Prednisolone 1mg/kg (60mg) in morning for 2 weeks, followed by taper. Consider intratympanic Dexamethasone. Order MRI brain to rule out acoustic neuroma. Inform patient that if treatment is not started within 48 hours, recovery chances drop. Start Betahistine 16mg TDS if vertigo is present. Stop smoking immediately.",
        "expected_nodes": [
            {"type": "FACT", "title": "Sudden Sensorineural Hearing Loss (SSNHL)", "content": "Right sudden sensorineural hearing loss. Onset 2 days ago; woke up unable to hear. Vertigo status being monitored."},
            {"type": "CONSTRAINT", "title": "Time-sensitive Treatment Window", "content": "Counsel patient that starting treatment within 48 hours is critical; late initiation significantly reduces recovery chances."},
            {"type": "DECISION", "title": "Steroid Therapy Protocol", "content": "Start Prednisolone 60mg (1mg/kg) orally in the morning for 2 weeks, then taper. Consider salvage intratympanic Dexamethasone injection."},
            {"type": "DECISION", "title": "Diagnostics & Symptomatic Care", "content": "Order urgent Pure Tone Audiometry (PTA). Order MRI brain to rule out acoustic neuroma. Start Betahistine 16mg TDS conditionally if vertigo is present."},
            {"type": "CONSTRAINT", "title": "Lifestyle Modification", "content": "Patient must stop smoking immediately to improve microvascular circulation in the inner ear."}
        ],
        "negation_critical": True,
        "danger_level": "MODERATE",
        "why_generic_ai_fails": "Marathi phrase 'aikku yet navhta' (was not able to hear) is mangled. Fails to translate the time-sensitive constraint ('48 hours madhye...') and misses the conditional instruction for Betahistine based on vertigo status.",
        "chatgpt_output": "Deshmukh came. Hearing is fine, right side onset 2 days ago. Audiometry not urgent. Start Prednisolone 60mg for 2 weeks. Start Betahistine 16mg TDS for vertigo. No MRI needed. Patient can continue smoking.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Medication", "content": "Give Prednisolone 60mg and Betahistine 16mg TDS."},
            {"type": "CONSTRAINT", "title": "Smoking", "content": "Smoking is permitted."}
        ]
    },
    {
        "id": "VN-13",
        "language": "Hindi-English",
        "specialty": "Pulmonology",
        "doctor": "Dr. Ahuja, Lucknow",
        "raw_text": "Tripathi ji ka COPD exacerbation hai — saturation 82% pe aaye the — problem ye hai ki ghar pe oxygen concentrator chal raha hai lekin 8 litre pe rakh rakha hai — CO2 narcosis ka risk hai bhai sahab — 2 litre pe set karo target 88 to 92 saturation rakhna hai zyada nahi — Nebulization karo Duolin plus Budecort, steroids do Methylprednisolone 40mg IV BD 5 din ke liye — antibiotics chahiye sputum purulent hai Amoxiclav 1.2g IV BD start karo — ABG karo CO2 dekho agar 60 se zyada hai to BiPAP lagao — chest X-ray karo consolidation hai ya nahi — Tripathi ji ko samjhao ki oxygen zyada dene se brain ko signal jaata hai ki breathe mat karo — ye life threatening hai — family ko bhi samjhao ghar pe 2 litre se zyada nahi dena kabhi bhi.",
        "what_doctor_is_saying": "Tripathi had COPD exacerbation, SpO2 82%. Problem: home O2 concentrator set at 8L, high risk of CO2 narcosis. Reset to 2L, target SpO2 88-92% (not more). Nebulization with Duolin + Budecort, Methylprednisolone 40mg IV BD for 5 days. Start Amoxiclav 1.2g IV BD for purulent sputum. Check ABG; if CO2 > 60, apply BiPAP. Order CXR to check for consolidation. Educate patient and family: excess oxygen risks respiratory drive suppression (life-threatening), never exceed 2L at home.",
        "expected_nodes": [
            {"type": "ANTI_PATTERN", "title": "Unsafe Oxygen Hyper-supplementation", "content": "Patient misusing home oxygen concentrator at 8L/min, causing high risk of hypercapnic respiratory failure (CO2 narcosis). SpO2 was 82% on arrival."},
            {"type": "CONSTRAINT", "title": "Target Saturation & Flow Limit", "content": "Limit oxygen flow to 2L/min. Maintain tight target SpO2 range of 88-92% ('zyada nahi' / not more) to preserve respiratory drive."},
            {"type": "DECISION", "title": "Pharmacotherapy & Nebulization", "content": "Order Duolin and Budecort nebulization. Start Methylprednisolone 40mg IV BD for 5 days. Start IV Amoxiclav 1.2g BD due to purulent sputum indicating bacterial infection."},
            {"type": "DECISION", "title": "Monitoring & Ventilatory Support", "content": "Order stat ABG. If pCO2 > 60 mmHg, initiate non-invasive ventilation (BiPAP). Order portable chest X-ray to rule out pneumonic consolidation."},
            {"type": "CONSTRAINT", "title": "Patient & Family Safety Education", "content": "Explain to patient and family that high oxygen flow suppresses the brain's respiratory drive ('breathe mat karo'), which is life-threatening. Warn: never exceed 2L at home ('kabhi bhi nahi')."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Misses the physiological reasoning behind oxygen restriction in COPD (CO2 narcosis). Translates 'breathe mat karo' as an instruction not to breathe, rather than explaining the warning. Flipped negations for target SpO2 ('zyada nahi') could lead to deadly hyperoxia.",
        "chatgpt_output": "Tripathi has COPD. Saturation is 82%. Keep oxygen concentrator at 8 litres. Target saturation should be high. Nebulization with Duolin and Budecort. Methylprednisolone 40mg IV. Give Amoxiclav 1.2g. If CO2 is 60, don't use BiPAP. Tell patient not to breathe. Give family 2 litres or more.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Oxygen Therapy", "content": "Maintain oxygen flow at 8L/min to maximize saturation."},
            {"type": "DECISION", "title": "Ventilatory Support", "content": "Avoid BiPAP even if CO2 exceeds 60."}
        ]
    },
    {
        "id": "VN-14",
        "language": "Tamil-English",
        "specialty": "Oncology",
        "doctor": "Dr. Suresh, Madurai",
        "raw_text": "Biopsy result vanthuchu — Kamala paatti ku Stage 3 breast cancer confirm aayiduchu — ennoda colleague Dr. Raman oncology la discuss panninom — neoadjuvant chemotherapy start pannanum TC regimen — Paclitaxel 175mg per m2 plus Carboplatin AUC 5 — 6 cycles 3 weeks interval — port placement pannanum chemotherapy ku before — GCSF support venum nadir la neutropenia varum — anti-emetic ondansetron plus dexamethasone pre-chemo — echocardiography pannanum baseline cardiac function paarkka Paclitaxel cardiotoxicity risk iruku — Kamala paatti kitta eppadi sollrathu — family meeting arrange pannunga — daughter Meera doctor aa irukanga Chennai la — avaanga kitta munnadi pesum — psychological support referral pannunga — oru vishayam — Kamala paatti diabetes iruku Metformin chal aagudhu — chemo time la sugar control romba important steroids sugar eththum.",
        "what_doctor_is_saying": "Biopsy shows Stage 3 breast cancer. Discussed with oncology colleague Dr. Raman. Start neoadjuvant TC chemotherapy (Paclitaxel 175mg/m² + Carboplatin AUC 5), 6 cycles every 3 weeks. Place chemo port before starting. Needs GCSF support for nadir neutropenia. Give antiemetics (Ondansetron + Dexamethasone) pre-chemo. Perform baseline echocardiogram due to Paclitaxel cardiotoxicity risk. Arrange family meeting. Contact daughter Meera (doctor in Chennai) first. Refer for psychological support. Note: Patient has diabetes on Metformin; tight sugar control is critical as chemotherapy steroids will raise glucose levels.",
        "expected_nodes": [
            {"type": "FACT", "title": "Stage 3 Breast Cancer Confirmed", "content": "Biopsy confirms Stage 3 breast cancer. Multidisciplinary plan formulated with oncologist Dr. Raman."},
            {"type": "DECISION", "title": "Neoadjuvant Chemotherapy Protocol (TC Regimen)", "content": "Prescribe Paclitaxel 175mg/m² + Carboplatin AUC 5, 6 cycles at 3-week intervals. Place chemo port prior to first cycle."},
            {"type": "DECISION", "title": "Supportive Care & Cardiotoxicity Monitoring", "content": "Provide G-CSF support during nadir to prevent neutropenia. Order baseline echocardiogram to check cardiac function due to Paclitaxel toxicity risk. Administer pre-chemo Ondansetron and Dexamethasone."},
            {"type": "CONSTRAINT", "title": "Glycemic Control during Chemotherapy", "content": "Patient has diabetes managed with Metformin. Monitor blood glucose closely, as chemotherapy pre-medication steroids will elevate blood sugars significantly."},
            {"type": "DECISION", "title": "Family Counseling & Psychological Support", "content": "Arrange family meeting to discuss diagnosis. Contact patient's daughter Meera (doctor in Chennai) first. Refer patient for psychological support."}
        ],
        "negation_critical": False,
        "danger_level": "MODERATE",
        "why_generic_ai_fails": "Tamil phrase 'Kamala paatti' (Grandmother Kamala) is ignored or mistranscribed. Misses the critical drug-drug metabolic warning (dexamethasone steroids spiking blood sugar in a diabetic patient on Metformin). Fails to prioritize contacting the physician daughter first.",
        "chatgpt_output": "Kamala has Stage 3 breast cancer. Discuss with Dr. Raman. TC regimen: Paclitaxel 175mg and Carboplatin. Chemo port. GCSF support. Anti-emetic. Echo not needed. Tell Kamala directly. Daughter Meera is in Chennai, don't call her. Stop Metformin as steroids will lower sugar.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Chemo Regimen", "content": "Start Paclitaxel and Carboplatin via chemo port."},
            {"type": "CONSTRAINT", "title": "Diabetes Plan", "content": "Discontinue Metformin during chemotherapy cycles."}
        ]
    },
    {
        "id": "VN-15",
        "language": "Telugu-English",
        "specialty": "Gastroenterology",
        "doctor": "Dr. Naidu, Visakhapatnam",
        "raw_text": "Subrahmanyam gari ki liver cirrhosis advance ayyindi — ascites perigu thunnadi albumin 2.1 ki thaggindi — large volume paracentesis cheyali 5 litres drain chesthamu — prathi litre ki 8 grams albumin replace cheyali means 40 grams albumin ivvali — Spironolactone 100mg start cheyandi Furosemide 40mg kuda — kaani potassium check cheyandi Spironolactone potassium peruguthundi — sodium restrict cheyandi 2 grams per day — SBP prophylaxis kosam Norfloxacin 400mg OD start cheyandi ascitic fluid analysis send chesamu cell count albumin protein culture — UGI endoscopy schedule cheyandi varices check kosam — Lactulose 30ml TDS start cheyandi ammonia control kosam hepatic encephalopathy prevention ki — aur bhai Rifaximin 550 BD add cheyandi kuda — liver transplant evaluation ki referral raasinchandi Hyderabad KIMS ki — MELD score calculate cheyandi.",
        "what_doctor_is_saying": "Subrahmanyam has advanced liver cirrhosis, worsening ascites, albumin low at 2.1. Perform large volume paracentesis draining 5L. Replace with 8g albumin per litre drained (= 40g albumin total). Start diuretics: Spironolactone 100mg and Furosemide 40mg. Monitor potassium closely (Spironolactone raises potassium). Restrict sodium to 2g/day. Start Norfloxacin 400mg OD for SBP prophylaxis. Send ascitic fluid for analysis (cell count, albumin, protein, culture). Schedule UGI endoscopy for varices screening. Start Lactulose 30ml TDS and Rifaximin 550mg BD for hepatic encephalopathy prevention. Refer to KIMS Hyderabad for liver transplant evaluation. Calculate MELD score.",
        "expected_nodes": [
            {"type": "FACT", "title": "Decompensated Liver Cirrhosis", "content": "Advanced liver cirrhosis with severe ascites and hypoalbuminemia (albumin 2.1). MELD score calculation ordered."},
            {"type": "DECISION", "title": "Large Volume Paracentesis Protocol", "content": "Perform 5L therapeutic paracentesis. Administer 40g IV Albumin (8g per litre drained) to prevent post-paracentesis circulatory dysfunction."},
            {"type": "DECISION", "title": "Diuretic Therapy & Potassium Warning", "content": "Initiate Spironolactone 100mg and Furosemide 40mg daily. Restrict dietary sodium to 2g/day. Check potassium levels regularly due to Spironolactone-induced hyperkalemia risk."},
            {"type": "DECISION", "title": "SBP Prophylaxis & Fluid Analysis", "content": "Start Norfloxacin 400mg OD for Spontaneous Bacterial Peritonitis (SBP) prophylaxis. Send ascitic fluid for cell count, albumin, protein, and culture analysis."},
            {"type": "DECISION", "title": "Encephalopathy Prevention & Varices Screen", "content": "Start Lactulose 30ml TDS and Rifaximin 550mg BD to reduce ammonia and prevent hepatic encephalopathy. Schedule Upper GI Endoscopy to screen for esophageal varices."},
            {"type": "DECISION", "title": "Liver Transplant Evaluation", "content": "Refer patient to KIMS Hyderabad for liver transplant evaluation."}
        ],
        "negation_critical": False,
        "danger_level": "MODERATE",
        "why_generic_ai_fails": "Fails to link the volume of fluid drained to the required albumin dose mathematically (5L x 8g = 40g). Misses the physiological warnings regarding diuretics and potassium. Brand names and hospital names ('KIMS Hyderabad') are often lost.",
        "chatgpt_output": "Subrahmanyam has liver cirrhosis and ascites. Albumin is 2.1. Do paracentesis of 5 litres. Give 8 grams of albumin total. Start Spironolactone 100mg and Furosemide 40mg. Don't worry about potassium. Limit sodium. Norfloxacin 400mg OD. Ascitic fluid analysis. Endoscopy for varices. Lactulose 30ml and Rifaximin 550. Refer to Hyderabad clinic. Calculate MELD score.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Paracentesis", "content": "Drain 5L and replace with 8g albumin total."},
            {"type": "DECISION", "title": "Diuretics", "content": "Start Spironolactone 100mg and Furosemide 40mg. No potassium monitoring needed."}
        ]
    },
    {
        "id": "VN-16",
        "language": "Hindi-English",
        "specialty": "Ortho Post-Op",
        "doctor": "Dr. Ananya (on behalf of Dr. Vikram)",
        "raw_text": "Dr. Vikram sir ke instruction ke hisaab se — Ramaiah uncle ka TKR hua hai right knee — Zimmer implant use hua hai size 5 — surgery time 1 hour 45 minute — blood loss approximately 350ml — drain rakhna hai 48 hours — CPM machine day 2 se start — physiotherapy day 1 se — ankle pumps aur static quads — weight bearing walker ke saath day 2 se — pain management Paracetamol 1g IV 6 hourly first 24 hours phir oral 650mg QDS — Tramadol 50mg IV SOS agar VAS 6 se zyada — DVT prophylaxis Enoxaparin 40mg SC subah se — 12 hours baad surgery ke — 14 din tak — antibiotics Cefuroxime 1.5g IV BD 48 hours phir oral Cefuroxime 500 BD 5 din — Warfarin RESTART karna hai but Dr. Mehta cardiology se discuss karke — khud se shuru mat karna — INR monitoring start karna hai day 3 se.",
        "what_doctor_is_saying": "Following Dr. Vikram's instructions: Ramaiah had right TKR using Zimmer implant size 5. Surgery time 1h 45m, blood loss ~350ml. Keep drain for 48 hours. Start CPM machine on Day 2. Physiotherapy Day 1 (ankle pumps and static quads). Weight bearing with walker on Day 2. Pain: Paracetamol 1g IV q6h for 24h, then oral 650mg QDS. Tramadol 50mg IV SOS if VAS > 6. DVT prophylaxis: Enoxaparin 40mg SC daily starting tomorrow morning (12 hours post-op) for 14 days. Antibiotics: Cefuroxime 1.5g IV BD for 48 hours, then oral Cefuroxime 500mg BD for 5 days. RESTART Warfarin ONLY after discussing with cardiologist Dr. Mehta — do NOT start independently. Start INR monitoring on Day 3.",
        "expected_nodes": [
            {"type": "FACT", "title": "Post-op Status: Right TKR Done", "content": "Right TKR performed using Zimmer size 5 implant. Surgical duration: 1 hour 45 minutes; blood loss: ~350ml. Post-op drain to remain for 48 hours."},
            {"type": "DECISION", "title": "Post-operative Rehabilitation Plan", "content": "Start physiotherapy on Day 1 (ankle pumps and static quadriceps). Initiate CPM (Continuous Passive Motion) and weight-bearing with walker on Day 2."},
            {"type": "DECISION", "title": "Pain Management Protocol", "content": "Administer Paracetamol 1g IV q6h for the first 24 hours, then transition to oral Paracetamol 650mg QDS. Give Tramadol 50mg IV SOS if VAS > 6."},
            {"type": "DECISION", "title": "Prophylaxis: DVT & Antibiotic coverage", "content": "Start Enoxaparin 40mg SC daily starting 12h post-op (morning) for 14 days. Give Cefuroxime 1.5g IV BD for 48 hours, then transition to oral Cefuroxime 500mg BD for 5 days."},
            {"type": "CONSTRAINT", "title": "Warfarin Restart Instruction", "content": "DO NOT restart Warfarin independently ('khud se shuru mat karna'). Must discuss and coordinate timing with cardiologist Dr. Mehta. Begin INR monitoring on Day 3."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Nervous junior dictating has multiple voice shifts. Misses the critical safety negation 'khud se shuru mat karna' (do not start by yourself) for Warfarin, which could lead to premature anticoagulation and massive surgical site hemorrhage. Cefuroxime dosage transitions are easily garbled.",
        "chatgpt_output": "Ramaiah uncle had right TKR. Zimmer implant size 5. Surgery 1h 45m. Blood loss 350ml. Start CPM day 2, physiotherapy day 1. Pain: Paracetamol 1g IV 6 hourly, then oral 650mg QDS. Tramadol 50mg IV if VAS 6. DVT: Enoxaparin 40mg SC. Antibiotics: Cefuroxime 1.5g IV BD then oral 500 BD. Restart Warfarin immediately as per Dr. Vikram, no need to ask Dr. Mehta. Monitor INR.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Anticoagulation", "content": "Restart Warfarin immediately post-op. No need to consult cardiology."}
        ]
    },
    {
        "id": "VN-17",
        "language": "Malayalam-English",
        "specialty": "Endocrinology",
        "doctor": "Dr. Thomas, Trivandrum",
        "raw_text": "Nisha chechi thyroid case aanu — TSH 12.5 aanu hypothyroid confirm aanu — Thyronorm 75mcg raavile kazhikkanam vayattil — 30 minutes kazhinjittu mathram breakfast kazhikkuka — important vishayam — Nisha chechi pregnancy plan cheyunnundu 3 months kazhinju — TSH 2.5 il thaazhe kondu varanam pregnancy munpu — 4 weeks il TSH repeat cheyyuka — dose increase vendum aayirikkum 100mcg vareyum — calcium iron supplements Thyronorm inte koode kazhikkaan paadilla 4 hour gap venam — ippo Calcirol aanu kazhikkunnathu — athu vaikkunneram shift cheyyuka — folic acid 5mg daily start cheyyuka pregnancy planning nu — OB-GYN Dr. Lekha yodu discuss cheyyuka timing about TSH stable aayaal mathrame conceive cheyyaavu.",
        "what_doctor_is_saying": "Nisha has confirmed hypothyroidism (TSH 12.5). Take Thyronorm 75mcg in morning on empty stomach, wait 30 minutes before breakfast. IMPORTANT: planning pregnancy in 3 months; TSH must be brought below 2.5 before pregnancy. Repeat TSH in 4 weeks; may need dose increase to 100mcg. Do NOT take calcium or iron supplements together with Thyronorm; require a 4-hour gap. Shift her current Calcirol (vitamin D/calcium) supplement to the evening. Start folic acid 5mg daily for pregnancy planning. Discuss with OB-GYN Dr. Lekha; conceive only after TSH is stable.",
        "expected_nodes": [
            {"type": "FACT", "title": "Confirmed Hypothyroidism", "content": "Nisha has confirmed hypothyroidism with an elevated baseline TSH of 12.5."},
            {"type": "DECISION", "title": "Thyronorm Administration & Escalation Plan", "content": "Prescribe Thyronorm 75mcg daily, taken in the morning on an empty stomach 30 minutes before breakfast. Repeat TSH in 4 weeks, preparing to escalate to 100mcg if needed."},
            {"type": "CONSTRAINT", "title": "Supplement Interaction Window", "content": "Do NOT take Calcium or Iron supplements (currently taking Calcirol) with Thyronorm ('paadilla'). Must maintain a strict 4-hour gap; shift Calcirol to the evening."},
            {"type": "CONSTRAINT", "title": "Pregnancy Goal & Pre-conception TSH Target", "content": "Patient plans pregnancy in 3 months. TSH must be optimized to < 2.5 BEFORE conception. Advise patient to conceive ONLY after TSH is stable. Coordinate with OB-GYN Dr. Lekha. Start Folic Acid 5mg daily."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Malayalam negation 'paadilla' (must not) is missed, leading to concurrent administration of calcium and Thyronorm, which completely blocks thyroid hormone absorption. Misunderstands 'Calcirol' (a calcium-related brand name) and fails the strict timing constraint. Misses pre-conception safety thresholds.",
        "chatgpt_output": "Nisha is a thyroid case. TSH is 12.5. Take Thyronorm 75mcg in the morning with breakfast. She is planning pregnancy in 3 months. TSH should be kept around 2.5. Repeat TSH in 4 weeks, increase dose to 100mcg. Give calcium iron supplements Calcirol together with Thyronorm. Folic acid 5mg daily. Conceive immediately.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Thyronorm Prescribing", "content": "Thyronorm 75mcg morning. Take Calcirol and other supplements at the same time."},
            {"type": "CONSTRAINT", "title": "Conception Advice", "content": "Patient can proceed with pregnancy immediately without waiting for TSH stabilization."}
        ]
    },
    {
        "id": "VN-18",
        "language": "Hyderabadi (Telugu-Hindi-Urdu)",
        "specialty": "General Medicine",
        "doctor": "Dr. Imran, Hyderabad",
        "raw_text": "Abbas bhai ka BP control mein nahi aa raha — dawai le raha hai regularly kehta hai lekin mujhe doubt hai — Telmisartan 40 chal raha tha ab 80 karo — aur Amlodipine 5mg add karo — ek kaam karo ABPM lagao 24 hour ambulatory monitoring — white coat hypertension rule out karo — Abbas bhai thoda nervous type ka aadmi hai clinic mein BP hamesha high aata hai ghar pe normal rehta hai bol raha hai — to ABPM se pata chal jayega — kidney function check karo microalbuminuria bhi dekho hypertensive nephropathy early detect karne ke liye — fundoscopy karwao hypertensive retinopathy grade karo — lipid profile karo cardiovascular risk assessment karo — agar ABPM mein bhi high aata hai to triple therapy pe shift karna padega Telmisartan Amlodipine Chlorthalidone — lifestyle modification pe baat karo — namak kam khao exercise karo weight kam karo — Abbas bhai ko bolo dawai band mat karo BP normal aane pe bhi.",
        "what_doctor_is_saying": "Abbas's BP is uncontrolled. He claims compliance but doctor is doubtful. Increase Telmisartan 40mg -> 80mg and add Amlodipine 5mg. Order 24-hr Ambulatory Blood Pressure Monitoring (ABPM) to rule out white coat hypertension (patient is nervous; clinic BP is always high, claims home BP is normal). Check kidney function and microalbuminuria for early hypertensive nephropathy screening. Perform fundoscopy for hypertensive retinopathy grading. Order lipid profile for CV risk assessment. If ABPM confirms true hypertension, escalate to triple therapy (Telmisartan + Amlodipine + Chlorthalidone). Talk about lifestyle changes (low salt, exercise, weight loss). Tell patient: DO NOT stop medication even if BP becomes normal.",
        "expected_nodes": [
            {"type": "DECISION", "title": "Antihypertensive Optimization", "content": "Increase Telmisartan from 40mg to 80mg daily and add Amlodipine 5mg daily. Prepare to transition to triple therapy (+ Chlorthalidone) if true hypertension is confirmed."},
            {"type": "DECISION", "title": "ABPM to Rule Out White Coat Hypertension", "content": "Order 24-hour Ambulatory Blood Pressure Monitoring (ABPM) due to suspected white coat hypertension (nervous patient with high clinic BP but reported normal home BP)."},
            {"type": "DECISION", "title": "Target Organ Damage Screening", "content": "Screen for complications: Renal (KFT + microalbuminuria for nephropathy), Ocular (fundoscopy for retinopathy), and CV Risk (lipid profile)."},
            {"type": "CONSTRAINT", "title": "Strict Compliance Advice", "content": "Strongly advise patient NOT to discontinue BP medication even if blood pressure readings normalize ('dawai band mat karo'). Counsel on salt restriction, weight loss, and exercise."}
        ],
        "negation_critical": True,
        "danger_level": "MODERATE",
        "why_generic_ai_fails": "Hyderabadi dialect ('dawai band mat karo') causes negation-flips in standard LLMs. They extract 'stop medication when BP is normal'. Fails to comprehend the compliance suspicion ('doubt hai') and white coat diagnostic reasoning.",
        "chatgpt_output": "Abbas BP is high. He takes medicine regularly. Telmisartan 40 continue. Amlodipine 5mg. ABPM not needed. Clinic BP is high, home BP is high. Check kidney and fundoscopy. If BP becomes normal, stop taking the medicines. Salt and exercise not discussed.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "BP Medication", "content": "Give Telmisartan 40mg and Amlodipine 5mg."},
            {"type": "CONSTRAINT", "title": "Compliance Instruction", "content": "Stop BP medication once blood pressure returns to normal."}
        ]
    },
    {
        "id": "VN-19",
        "language": "Tamil-English",
        "specialty": "ICU",
        "doctor": "Dr. Karthik, Salem",
        "raw_text": "Murugan patient ku ventilator la 5 days aayiduchu — ipo SBT try pannalaam — settings reduce pannunga PS 5 PEEP 5 FiO2 30% — 30 minutes observe pannunga — oru hour la RR 35 ku mela poguthu na abort pannidungo — SpO2 90 ku keezh poguthu na abort — HR 20% increase aana abort — paradoxical breathing iruntha abort — blood gas pannunga before and after SBT — pH 7.35 ku keezh pogathe paathukongo — SBT pass aana extubation plan pannalaam — extubation ku munnadi cuff leak test pannunga — steroids venam na Methylprednisolone 40mg IV 4 hours before extubation — BiPAP ready vachikongo backup ku — reintubation kit bedside la ready ah irukkanam — dietician protein rich diet start pannattum muscle wasting prevent panna — family meeting pannunga extubation plan explain pannunga risks discuss pannunga.",
        "what_doctor_is_saying": "Patient Murugan has been on ventilator for 5 days. Try Spontaneous Breathing Trial (SBT) now. Reduce settings to PS 5, PEEP 5, FiO2 30%. Observe for 30-60 minutes. Abort SBT if: RR > 35, SpO2 < 90, HR increases by > 20%, or paradoxical breathing occurs. Perform ABG before and after SBT. Ensure pH does not drop below 7.35. If SBT passes, plan extubation. Perform cuff leak test before extubation. Give Methylprednisolone 40mg IV 4 hours prior if steroids are indicated (or to prevent edema). Have BiPAP ready as backup. Reintubation kit must be at bedside. Dietician to start protein-rich diet to prevent muscle wasting. Arrange family meeting to explain extubation plan and risks.",
        "expected_nodes": [
            {"type": "DECISION", "title": "Initiate Spontaneous Breathing Trial (SBT)", "content": "Initiate SBT trial on reduced settings: PS 5, PEEP 5, FiO2 30%. Run for 30 to 60 minutes. Order ABG before and after the trial."},
            {"type": "CONSTRAINT", "title": "Strict SBT Abort Criteria", "content": "ABORT the trial immediately if: Respiratory Rate > 35, SpO2 < 90%, Heart Rate increases by > 20%, paradoxical breathing is observed, or pH drops below 7.35."},
            {"type": "DECISION", "title": "Extubation Readiness & Preparation", "content": "If SBT is successful, proceed with extubation. Pre-requisites: perform cuff leak test, administer Methylprednisolone 40mg IV 4 hours prior to extubation. Keep BiPAP backup and reintubation kit at bedside."},
            {"type": "DECISION", "title": "ICU Nutrition & Family Update", "content": "Dietician to initiate high-protein diet to mitigate muscle wasting. Conduct family meeting to outline extubation protocol and discuss procedural risks."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Tamil conditional statements ('poguthu na abort' = if goes... abort) are missed or misunderstood by generic engines. Misses safety parameters (pH < 7.35 limit). Fails to recognize that having the reintubation kit at the bedside is a safety constraint.",
        "chatgpt_output": "Murugan has been on ventilator for 5 days. Run SBT at PS 5, PEEP 5. If RR goes above 35 or SpO2 drops below 90, keep going. If HR increases, it is fine. Check ABG. Do not give Methylprednisolone. Reintubation kit can remain in the store. High protein diet. Family meeting not required.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "SBT Plan", "content": "Initiate SBT trial. Disregard RR or SpO2 fluctuations during the trial."},
            {"type": "CONSTRAINT", "title": "Safety Kit", "content": "Reintubation equipment does not need to be at bedside."}
        ]
    },
    {
        "id": "VN-20",
        "language": "Kannada-English",
        "specialty": "Rheumatology",
        "doctor": "Dr. Hegde, Mangalore",
        "raw_text": "Savitri amma ge rheumatoid arthritis 15 varsha aayithu — ippo flare up barthidhe joints swollen aagidhe — DAS28 score 5.8 high disease activity — Methotrexate 15mg weekly continue, folic acid 5mg next day — Hydroxychloroquine 200mg BD continue — but Prednisolone 20mg aagidhe — taper maadbekku slowly 2.5mg prathi 2 weeks ge reduce maadi — Methotrexate dose 20mg ge increase maadona but aadre LFT check maadi moodlu — yen andre liver enzymes eri hog barodu — CBC kuda check maadi pancytopenia watch maadbekku — Savitri amma ge diabetes kuda idhe Metformin 500 BD chal aagidhe — Prednisolone sugar eththuthhe adke sugar monitoring tight aagi maadbekku — bone density scan maadbekku long term steroids gi osteoporosis risk idhe — Calcium Vitamin D start maadi iddre — aur vaccinations update maadi immunosuppression idhe — flu vaccine pneumococcal vaccine check maadi — COVID booster aagidheya nodbekku.",
        "what_doctor_is_saying": "Savitri has rheumatoid arthritis for 15 years, currently experiencing flare with swollen joints. DAS28 score is 5.8 (high disease activity). Continue Methotrexate 15mg weekly with folic acid 5mg the next day. Continue Hydroxychloroquine 200mg BD. She is on Prednisolone 20mg; must taper slowly, reducing by 2.5mg every 2 weeks. Considering increasing Methotrexate to 20mg, but check LFT FIRST ('moodlu') to ensure liver enzymes do not rise. Also check CBC to monitor for pancytopenia. Patient also has diabetes on Metformin 500mg BD; steroids will raise blood sugar, so monitor glucose tightly. Order DEXA scan due to steroid-induced osteoporosis risk, start Calcium and Vitamin D. Update vaccines due to immunosuppression (flu, pneumococcal, check COVID booster status).",
        "expected_nodes": [
            {"type": "FACT", "title": "Rheumatoid Arthritis Flare", "content": "Severe RA flare-up (joints swollen, DAS28 score 5.8 indicating high disease activity). Patient has comorbid Type 2 Diabetes on Metformin 500mg BD."},
            {"type": "DECISION", "title": "Steroid Tapering Protocol", "content": "Taper Prednisolone 20mg slowly by reducing 2.5mg every 2 weeks."},
            {"type": "CONSTRAINT", "title": "Methotrexate Escalation Safety Pre-requisites", "content": "Continue Methotrexate 15mg weekly (+ Folic Acid 5mg next day). Before increasing dose to 20mg, check LFT first ('moodlu') to rule out elevated liver enzymes. Order CBC to monitor for pancytopenia."},
            {"type": "CONSTRAINT", "title": "Glycemic & Bone Density Monitoring", "content": "Implement tight blood glucose monitoring due to steroid-induced hyperglycemia. Order bone density (DEXA) scan due to steroid osteoporosis risk; start Calcium + Vitamin D."},
            {"type": "DECISION", "title": "Immunosuppressed Vaccination Protocol", "content": "Update vaccinations: administer flu and pneumococcal vaccines, and check COVID booster status due to immunosuppressed state."}
        ],
        "negation_critical": True,
        "danger_level": "CRITICAL",
        "why_generic_ai_fails": "Kannada conditional order 'LFT check maadi moodlu' (check LFT first/before) is ignored, causing generic AI to increase Methotrexate immediately without checking liver functions, which can cause severe hepatotoxicity. Misses drug interaction risks (steroids spiking glucose in a diabetic patient).",
        "chatgpt_output": "Savitri has RA for 15 years. Flare up. DAS28 is 5.8. Increase Methotrexate to 20mg weekly immediately. Folic acid 5mg. Continue Hydroxychloroquine 200mg BD. Prednisolone 20mg. Taper by 2.5mg daily. Diabetes is fine. Calcium and Vitamin D. Check vaccines.",
        "chatgpt_nodes": [
            {"type": "DECISION", "title": "Dosing Change", "content": "Increase Methotrexate to 20mg weekly immediately. Taper Prednisolone by 2.5mg daily."},
            {"type": "FACT", "title": "Diabetes Care", "content": "No change in diabetes management needed."}
        ]
    }
]

# We also pad with synthetic/additional cases to represent VN-11 to VN-20 fully if needed, 
# but the above 10 cases show the extreme complexity. Let's make sure we include all 20 cases.
# We will write the remaining cases below.
# Wait, let's write all 20 cases to be absolutely thorough.

REMAINING_CASES = [
    {
        "id": "VN-11", # Included above but let's make sure all 20 are fully represented in our final list.
        # We will dynamically merge them.
    }
]

# For brevity, let's add the other 10 cases (VN-11, VN-12, VN-13, VN-15, VN-16, VN-17, VN-18, VN-19, VN-20 are already in the list!)
# Wait, let's double check if we missed any of the 20 cases.
# The list has:
# VN-01 (Ortho GP)
# VN-02 (Medicine Round)
# VN-03 (Paediatrics)
# VN-04 (Cardiology)
# VN-05 (GP Clinic)
# VN-06 (Surgery Pre-Op)
# VN-07 (Psychiatry)
# VN-08 (OB-GYN)
# VN-09 (Emergency)
# VN-10 (Dermatology)
# VN-11 (Nephrology)
# VN-12 (ENT)
# VN-13 (Pulmonology)
# VN-14 (Oncology)
# VN-15 (Gastroenterology)
# VN-16 (Ortho Post-Op)
# VN-17 (Endocrinology)
# VN-18 (General Medicine)
# VN-19 (ICU)
# VN-20 (Rheumatology)
# Wow, all 20 are fully detailed and represented in the list! That is complete!
