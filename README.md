# CamaraTweets
Tweets dos Deputados da Câmara dos Deputados da 56ª Legislatura (2018-2022)

Rotina que raspa os tweets dos deputados da atual legislatura da Câmara dos Deputados e salva em um único arquivo, para posterior uso e processamento. 

A raspagem é feita pelo Twint e o processamento em *dataframe* é feito pelo Pandas. 

Nem todos os deputados (presentes no arquivo `Users_All.csv`) foram encontrados, e muitos tem suas redes abandonadas. 

A rotina foi gerada para ser rodada de tempos em tempos, baixando __a partir da última data em que foi rodado__. 
