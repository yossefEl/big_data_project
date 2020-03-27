lignes = LOAD 'hdfs://quickstart.cloudera:8020/user/cloudera/countword/textWord' AS (ligne : chararray) ; 
mots = FOREACH lignes GENERATE FLATTEN(TOKENIZE(ligne)) as mot;
grouped = GROUP mots BY mot ; 
wordcount = FOREACH grouped GENERATE group, COUNT(mots) as nbmot;
wordcountt = GROUP wordcount ALL ; 
somme = foreach wordcountt generate SUM(wordcount.nbmot) ;
STORE somme INTO 'results' USING JsonStorage();


