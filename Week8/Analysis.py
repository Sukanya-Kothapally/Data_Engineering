import matplotlib.pyplot as plt
import seaborn as sns

a = ('Totalcases','Poverty')
b = ('Totaldeaths','Poverty')
c = ('Totalcases','IncomePerCap')
d = ('Totaldeaths','IncomePerCap')
e = ('cases_dec','Poverty')
f = ('deaths_dec','Poverty')
g = ('cases_dec','IncomePerCap')
h = ('deaths_dec','IncomePerCap')


'''
For Oregon data

'''
oregondf= integrated_df.loc[integrated_df.index.get_level_values('state') == 'Oregon']
#Oregon_data.head(5)

cor=[]

cor.append(a)
cor.append(b)
cor.append(c)
cor.append(d)
cor.append(e)
cor.append(f)
cor.append(g)
cor.append(h)
# print(cor)

plots_oregon=[]
for row in cor:
    graph=(oregondf[row[0]].corr(integrated_df[row[1]]),row[0],row[1])
    plots_oregon.append(graph)
    
for i in plots_oregon:
    R=i[0]
    print("R for all corelations respectively", R)
    if(R>0.5 or R<-0.5):
        plt.figure()
        sns.scatterplot(data=oregondf,x=i[1],y=i[2]) # For Oregon Data
		
		
plots_all=[]   
for row in cor:
    graph=(integrated_df[row[0]].corr(integrated_df[row[1]]),row[0],row[1])
    plots_all.append(graph)

for i in plots_all:
    R=i[0]
    print("R for all corelations respectively", R)
    if(R>0.5 or R<-0.5):
        plt.figure()
        sns.scatterplot(data=integrated_df,x=i[1],y=i[2]) #for others