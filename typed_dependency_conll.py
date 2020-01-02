def TypeDependencyToConll(filename):
	with open(filename) as f:
		text=f.read()
	from nltk import sent_tokenize,word_tokenize
	import nltk
	sents=sent_tokenize(text)
	ss=sents[0].splitlines()
	kk=[]
	for i in range(len(ss)):
		kk.append(nltk.word_tokenize(ss[i]))
	name=[]
	card_num=[]
	lower_name=[]
	pos_tags=[]
	rel=[]
	u_pos=[]
	empty=[]
	from nltk.stem import WordNetLemmatizer
	lemmatizer=WordNetLemmatizer()
	import spacy
	import pandas as pd
	sp=spacy.load('en_core_web_sm')
	for i in range(len(ss)):
		name.append(kk[i][4].split('-')[0])
		card_num.append(kk[i][2].split('-')[1])
		lower_name.append(lemmatizer.lemmatize(name[i],pos='v'))
		pos_tags.append(nltk.pos_tag(lower_name)[i][1])
		rel.append(kk[i][0])
		empty.append('_')
		sen=sp(kk[i][4].split('-')[0])
		u_pos.append(sen[0].pos_)
	#print(pd.DataFrame(OrderedDict({'Name':name,'Lower_name':lower_name,'UNI_POS':u_pos,'pos':pos_tags,'empty':empty,'CARD_NUM':card_num,'relation':rel,'empty1':empty,'empty2':empty})))
	#print(pd.DataFrame([*zip(name,lower_name,u_pos,pos_tags,empty,card_num,rel,empty,empty)]))
	df=pd.DataFrame([*zip(name,lower_name,u_pos,pos_tags,empty,card_num,rel,empty,empty)])
	with open("E_conversion_to_conll.txt", 'a') as k:
	    k.write(df.to_string(header = True, index = True))
TypeDependencyToConll('Desktop/sent.txt')
