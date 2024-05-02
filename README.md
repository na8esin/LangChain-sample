# hello
## 環境構築
python -m venv .venv

source .venv/bin/activate

pip install --upgrade --quiet -r requirements.txt

## 詳細
https://python.langchain.com/docs/integrations/llms/bedrock/

```
Claude v3 models are not supported by this LLM.Please use `from langchain_community.chat_models import BedrockChat` instead.
```
BedrockはBedrockChatに変更

`https://python.langchain.com/docs/get_started/quickstart/`
この辺りも参考

## sql
https://python.langchain.com/docs/use_cases/sql/quickstart/

`ModuleNotFoundError: No module named 'MySQLdb'`

https://github.com/PyMySQL/mysqlclient/blob/main/README.md#macos-homebrew

以前、mysql-clientをmac portsでインストールした気がするので、割愛

ここで、mysqlclientをrequirements.txtに追加して、下記実行
`pip install --upgrade --quiet -r requirements.txt`

```
Exception: Can not find valid pkg-config name.
```
みたいなエラーが出てうまくいかない


`sudo port install pkgconfig`

package名と違うのやだね。
```
which pkg-config
/opt/local/bin/pkg-config
```

`export PKG_CONFIG_PATH="/opt/local/lib/mysql8/pkgconfig"`

うーんうまく帰ってこない
```
To get the total number of products, we can run the following SQL query:

SELECT COUNT(*) AS total_products
FROM products;
```

langchainが裏で生成してくれているプロンプトを確認
```
You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

Only use the following tables:
{table_info}

Question: {input}
```

```
LangChainDeprecationWarning: The class `BedrockChat` was deprecated in LangChain 0.0.34 and will be removed in 0.3. An updated version of the class exists in the langchain-aws package and should be used instead. To use it run `pip install -U langchain-aws` and import as `from langchain_aws import ChatBedrock`.
```

```
LangChainDeprecationWarning: The method `Chain.__call__` was deprecated in langchain 0.1.0 and will be removed in 0.2.0. Use invoke instead.
```

## poetry入れてみた
`poetry run which python`を実行すると`.venv/bin/python`を指し示す

`poetry add $( cat requirements.txt )`でやってみたけど、長くなりすぎてダメな気がする

## alembic
`alembic init alembic`