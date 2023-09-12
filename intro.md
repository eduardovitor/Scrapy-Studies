
Scrapy é um framework open-source para extração de dados de páginas web. A extração de dados pode ocorrer de duas formas: xpath e css. Antes de codar, é possível extrair dados da página para teste usando o scrapy shell. Site referência usado para estudo do scraping : 
[Quotes To Scrape](https://quotes.toscrape.com/)

## Abrindo o scrapy shell

``` 
scrapy shell {{website_url}}
```
## Exemplos de extração com xpath

- ```response.xpath("//div")``` : Extrai todas as divs da página;
- ```response.xpath("//div/span")```: Extrai todos os elementos span dentro de div;
- ```response.xpath("//div/span[@class='text']")```: Extrai os elementos span com a classe text;
- ```response.xpath("//div/span[@class='text']/text()")```: Extrai os seletores de elementos span com a classe text e seus respectivos conteúdos de texto;
- ```response.xpath("//div/span[@class='text']/text()").getall()```: Extrai apenas os textos dos elementos span com a classe text.

## Exemplos de extração com css

- ```response.css("small")``` : Extrai todos os elementos small da página;
- ```response.css("small.author")```: Retorna todos os elementos small que têm como classe author;
- ```response.css("small.author::text")```: Retorna todos os elementos small da classe author e seus respectivos conteúdos de texto;
- ```response.css("small.author::text").getall()```: Extrai apenas o texto de todos os elementos small.