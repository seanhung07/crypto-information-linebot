# Crypto Information Linebot
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/logo.png" width="100" height="100">

## Join the Line Bot
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/qrcode.png" width="150" height="150">

查詢以下內容：
- 板塊分佈
- 恐懼與貪婪指標
- 漲跌分佈
- 市值前十/市占率
- 每日新聞
- 市場情況

## Example

<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/4.png" width="500" height="400">
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/1.png" width="500" height="600">
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/2.png" width="500" height="200">
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/3.png" width="500" height="400">

## How to create Line Bot

1. Login in to https://developers.line.biz/  </br> Choose Messagging API

<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/explain1.png">

2. Create new Providers (green button: Create)

<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/create.png">

3. Enabled bot join group chat and Disabled Auto-reply messages

<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/setting.png">

4. Channel Secrets and Channel access token

<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/explain2.png">
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/access.png">

## Create Heroku Account

### Install Heroku Cli
- MacOS 
```
brew tap heroku/brew && brew install heroku
```
- Linux
```
sudo snap install --classic heroku
```
- Windows
  - [64-bit](https://cli-assets.heroku.com/heroku-x64.exe)
  - [32-bit](https://cli-assets.heroku.com/heroku-x86.exe)
## Heroku CLi Login
```
heroku login
```
<img src = "https://github.com/seanhung07/crypto-information-linebot/blob/main/img/login.png">

```
heroku git:remote -a [your heroku app name]
heroku git:remote -a sean-crypto-information
```
## Upload your project to Heroku

```
git add .
git commit -am'any description'
git push heroku master
```
