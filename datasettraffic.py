import twint

user = ['ATCSKotaSMG']
for x in user :
    c = twint.Config()
    c.Username = x
    c.Format = "Username: {username} | Tweet: {tweet} |" 
    c.Store_csv = True 
    c.Output = "trafficsmg_dataset.csv" 
    twint.run.Search(c)

