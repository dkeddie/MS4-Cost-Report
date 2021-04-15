// /*
//     Core logic/payment flow for this comes from here:
//     https://stripe.com/docs/payments/accept-a-payment
//     CSS from here: 
//     https://stripe.com/docs/stripe-js
// */

function card(stripe_public_key, customer_email) {
  document.addEventListener("DOMContentLoaded", function (event) {
    var stripe = Stripe(stripe_public_key);
    var elements = stripe.elements();

    var style = {
      base: {
        iconColor: '#c4f0ff',
        color: '#000',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '14px',
        fontSmoothing: 'antialiased',
        // ':-webkit-autofill': {
        //   color: '#fce883',
        // },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#FFC7EE',
        color: '#FFC7EE',
      },
    };

    var card = elements.create('card', { style: style });
    card.mount("#card-element");

    card.on('change', function (event) {
        displayError(event);
      });
      
      function displayError(event) {
        // changeLoadingStatePrices(false);
        let displayError = document.getElementById('card-element-errors');
        if (event.error) {
          displayError.textContent = event.error.message;
        } else {
          displayError.textContent = '';
        }
      };

    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
      event.preventDefault();

      // Added steps to prevent double click 
      $('#checkout').prop('disabled', true)
      $('#card-element-errors').text("Payment in process... please be patient")

      stripe.createToken(card).then(function(result){
        if(result.error) {
          var errorElement = document.getElementById('card-element-errors');
          errorElement.textContent = result.error.message;
        } else {
          stripe.createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
              name: $.trim(form.customer_name.value),
              email: $.trim(form.customer_email.value),
              phone: $.trim(form.default_phone_number.value),
              address:{
                line1: $.trim(form.default_street_address1.value),
                line2: $.trim(form.default_street_address2.value),
                city: $.trim(form.default_town_or_city.value),
                country: $.trim(form.default_country.value),
                state: $.trim(form.default_county.value),
                postal_code: $.trim(form.default_postcode.value),
              } 
            },
          }).then(function(payment_method_result){
            if (payment_method_result.error) {
              var errorElement = document.getElementById('card-element-errors');
              errorElement.textContent = payment_method_result.error.message
            } else {
              var form = document.getElementById('payment-form');
              var hiddenInput = document.createElement('input');

              hiddenInput.setAttribute('type', 'hidden');
              hiddenInput.setAttribute('name', 'payment_method_id');
              hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

              form.appendChild(hiddenInput);

              form.submit();
            }
          })
        }
      })
    });

  })
}


// Confirmation of Details before Card Payment

var plan_id = $('input[name="stripe_plan_id"]').val()
var plan_name = ""

if (plan_id = "price_1IakCVLti2F8BZ1vMCS0D56C") {
  plan_name = "Daily @ £1 per day"
} else if (plan_id = "price_1IakBnLti2F8BZ1vmf00rG9b") {
  plan_name = "Monthly @ £10 per month"
} else {
  plan_name = "Yearly @ £100 per year"
}
$('input[name="subscription"]').val(plan_name)



