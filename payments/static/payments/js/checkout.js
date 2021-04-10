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

      stripe.createToken(card).then(function(result){
        if(result.error) {
          var errorElement = document.getElementById('card-element-errors');
          errorElement.textContent = result.error.message;
        } else {
          stripe.createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
              email: customer_email,
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

