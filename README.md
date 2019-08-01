# NetEase-cloud-music
网易云音乐评论解密

# 解密方式
整个过程有三个关键参数
key : 双方约定
iv : 双方约定
randkey : 前端生成( createrandkey(16)即可生成 )

# 1.第一次加密
使用 key 和 iv进行第一次AES加密
params是原始的json参数,比如是 要传的手机号
var params={"mobile":"13666666666"}
var params1 = aesEncrypt(JSON.stringify(params),key,iv)

# 2.第二次加密
使用 randkey 和 iv 进行第二次 AES加密
var params2 = aesEncrypt(params1,randkey,iv)

# 3.将randkey 和 加密params2 传输到服务端
即传两个参数即可
    {
        randkey:randkey,
        params:params2
    }
    
# 后端操作：
使用randkey 解密出 prams1
使用key     解密出 params
