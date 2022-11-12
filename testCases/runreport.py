title = "My New Report"
with open('C:/allure2/allure-generator/src/main/java/io/qameta/allure/summary/SummaryPlugin.java','r+') as report:
   x = report.read().replace("Allure Report", title)
with open('C:/allure2/allure-generator/src/main/java/io/qameta/allure/summary/SummaryPlugin.java','w+') as report:
    report.write(x)
