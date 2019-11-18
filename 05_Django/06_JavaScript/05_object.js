const me = {
  name: '창오',    // key가 한 단어일 때
  'phone number': '01022046899',    // key가 여러 단어일 때
  appleProducts: {
    iphone: 'xs',
    watch: 'series5',
    macbook: 'pro2019'
  }
}
me.name       // "창오"
me['name']    // "창오"
// Key가 여러 단어일 때 []로 접근!
me['phone number']    // "01022046899" 

me.appleProducts
// {iphone: "xs", watch: "series5", macbook: "pro2019"}
me.appleProducts.iphone
// "xs"