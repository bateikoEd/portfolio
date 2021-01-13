# Case
Потрібно побудувати модель на абонентах, цільова мітка по яким міститься у файлі train.csv.
<p>
Для цього вам необхідно використати дані з файлів tabular_data.csv та hashed_feature.csv. 
Після цього, використовуючи вашу модель, потрібно для абонентів з файлу test.csv заповнити колонку score – ймовірність того, 
що абонент відноситься до сегменту водіїв. Зверніть увагу, що необхідно спрогнозувати факт відношення до сегменту водіїв, без прив'язки до періоду.
</p>


Крок 3. Перевіряємо, що було завантажено і навіщо.

Архів містить 4 файли:

tabular_data.csv, hashed_feature.csv, train.csv, test.csv.

Для чого вони?
Ці файли допоможуть вирішити аналітичну задачу. Необхідно побудувати модель, що виявлятиме сегмент водіїв серед абонентів ПрАТ «Київстар».

## Це задача бінарної класифікації:
«1» – абонент являється водієм (відноситься до сегменту водіїв),
«0» – абонент не є водієм (не відноситься до сегменту водіїв).

#### Файли tabular_data.csv і hashed_feature.csv ̶ тут описові характеристики щодо 4084 абонентів («ID» – це ідентифікатор абонента).
#### Файл train.csv  ̶  це дані щодо цільової мітки (чи належить абонент до сегменту водіїв).
#### Файл test.csv  ̶  це список абонентів, для яких необхідно зробити прогноз, за яким ми й будемо оцінювати якість ваших моделей.

## А тепер детальніше:
» Файл tabular_data.csv містить числові дані щодо активності абонента за 12 періодів. 

• period – номер періоду (періоди послідовні, 1 – найновіший);
• id – ідентифікатор абонента;
• feature_0 – feature_49 – дані щодо активності абонента у відповідний період.

» Файл hashed_feature.csv – тут набір захешованих значень однієї категоріальної змінної для абонента.

• id – ідентифікатор абонента;
• feature_50 – хеш від значення категоріальної змінної.

» Файл train.csv – тут дані з цільовою міткою.

• id – ідентифікатор абонента;
• target – значення цільової мітки (1 – належить до сегменту водіїв, 0 – не належить до сегменту водіїв).

» Файл test.csv – список абонентів, для яких потрібно зробити передбачення за допомогою ваших моделей.

• id – ідентифікатор абонента;
• score – ймовірність того, що абонент належить до сегменту водіїв (класу «1»). Цю ймовірність визначає ваша модель


# Soluction 
- Short information about my research <br>
Explorary data analysis. <br>
Comparing dimensionaly reduction with PCA(choosin different variation value), LDA, corealation rang(Pearson and Spearman) and comparing. <br>
Balanced data set(removing from the sample). <br>
Working with outliers(define and delete). <br>
Comparing result from trained models. <br>




- [Jupyter notebook with research](https://github.com/bateikoEd/portfolio/blob/main/big_data_school/upgraded%20.ipynb)
- [First atempt (minimal data preparation)](https://github.com/bateikoEd/portfolio/blob/main/big_data_school/BateikoEduardPROGRAM.ipynb)
