import pandas as pd
                                  
df=pd.read_csv("C:/Users/Abhinay/Desktop/movie_dataset.csv")
df.columns
features=['keywords','cast','genres']
for feature in features:
    df[feature] = df[feature].fillna('')
    
def comb_features(row):
    try:
        return row['keywords']+" "+row['cast']+" "+row["genres"]
    except:
        print ("Error:", row)

df["comb_features"] = df.apply(comb_features,axis=1)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["comb_features"])

cosine_sim = cosine_similarity(count_matrix)
cosine_sim.shape
def get_title(index):
    return df[df.index == index]["title"].values[0]

def get_index(title):
    return df[df.title == title]["index"].values[0]


from tkinter import *
   
def show_data():
    txt.delete(0.0, 'end')
    movie =ent.get()
    movie_user_likes =movie        
    movie_index = get_index(movie_user_likes)
    i=int(movie_index)
    Similar_movies = list( enumerate(cosine_sim[i]))
                
    sorted_similar_movies = sorted(Similar_movies,key = lambda x:x[1], reverse = True)
    i=0;
    j=0;
    List =[None]*10
    for element in sorted_similar_movies:
            s=get_title(element[0])
            List[j]=s
            j=j+1;
            i=i+1;
            if i>=10:
                break
            
    for x in range(len(List) -1, -1, -1):
        t="\n"
        txt.insert(0.0, List[x])
        txt.insert(0.0, t)
           
root=Tk()
root.geometry("420x300")
l1 = Label(root, text="Please Type The Movie Name which You Liked :",bg="yellow")
l2 = Label(root, text="The Best Movies for You are :",bg="violet red")
ent =Entry(root)
l1.grid(row=0)
l2.grid(row=2)
ent.grid(row=0, column=1)
txt=Text(root,width=50,height=13, wrap=WORD,bg="sky blue")
txt.grid(row=3, columnspan=2, sticky=W)
               
btn=Button(root, text="Search", bg="aquamarine", fg="red", command=show_data)
btn.grid(row=1, columnspan=2)
root.mainloop()
