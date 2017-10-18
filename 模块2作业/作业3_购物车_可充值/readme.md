#### 购物车
1. 商品信息- 数量、单价、名称		商品信息通过列表的相互嵌套实现
2. 用户信息- 帐号、密码、余额		将用户信息保存至文件shopping_user
3. 用户可充值		对shopping_user中的余额进行修改
4. 购物历史信息			退出时查看已购买商品
5. 允许用户多次购买，每次可购买多件
6. 余额不足时进行提醒
7. 用户退出时 ，输出当次购物信息			购物车shopping_cart 字典输出
8. 用户下次登陆时可查看购物历史			判断是否购买过shopping_regular
   将用户此次购物信息存入到历史购物文件shopping_history
9. 商品列表分级显示			for循环打印

#### 文件说明
1. 历史购物文件 shopping_history
2. 用户信息文件 shopping_user
3. 老用户信息文件 shopping_regular
4. 用户备份信息 shopping_user_bak

#### 流程思路
1. 用户登录
    1. 通过shopping_user文件对用户名密码进行判断，进行登录
    2. 通过shopping_regular文件对用户名进行判断，标记老用户
2. 老顾客打印上次购物信息
    1. 通过用户名查找并遍历shopping_history，输出上次购物信息
3. 商品购买
    1. 判断购物车字典shopping_cart是否存在商品，如果存在，将数量
       做相应的增加，如果没有，则直接增加购买信息
    2. 判断是否购物，如果购物则将购物信息写入shopping_history
    3. 如果登陆时没有标记老客户，则将用户信息写入shopping_regular
4. 用户充值
    1. 每次购物流程结束后，会将用户余额回写到shopping_user文件中
#### 注：
商品购买结束时，会将购物信息写入shopping_history文件中，下次用户登录
会输出shopping_history文件中信息，但是写入过程中是以字典形式写入，
未能掌握字典相同键的合并，所以采取覆盖写入，即登录时只能查阅上一次
发生购买的购物信息
