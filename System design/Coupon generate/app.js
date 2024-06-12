// Define a function to generate a random coupon code
function generateCouponCode(length) {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let couponCode = '';
    for (let i = 0; i < length; i++) {
      couponCode += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return couponCode;
}

class Coupon {
  constructor(data) {
    this.name = data.name;
    this.expiration = data.name;
    this.discount = {
      maxDiscount: this.data.discount.maxDiscount,
      unit: this.data.discount.unit // percentage, number, 
    };
    this.redeemed = false
  }

  redeem() {
    if (isValid()) {
      this.redeemed = true;
      console.log(`Coupon ${this.code} redeemed for ${this.discount.maxDiscount}${this.discount.unit} discount.`)
    }
  }

  isValid() {
    return !this.redeemed && this.expiration > new Date();
  }
}
