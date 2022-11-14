select owner_id,owner_name,count(category_id)
from article inner join owner on article.owner_id = owner.owner_id 
inner join category_article_mapping on category_article_mapping.article_id = article.id;
