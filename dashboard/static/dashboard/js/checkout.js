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












// function createCustomer() {
//   let billingEmail = document.querySelector('#emailSub').value;
//   return fetch('/create-customer', {
//     method: 'post',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({
//       email: billingEmail,
//     }),
//   })
//     .then((response) => {
//       return response.json();
//     })
//     .then((result) => {
//       // result.customer.id is used to map back to the customer object
//       return result;
//     });
// }


// // Save Payment Details and create the subscription

// var form = document.getElementById('payment-form');

// form.addEventListener('submit', function (ev) {
//   ev.preventDefault();
// });

// function createPaymentMethod({ card }) {
//   const customerId = "cus_JDEfrTKbxTGFQf";
//   // Set up payment method for recurring usage
//   let billingName = document.querySelector('#nameSub').value;

//   let priceId = document.querySelector('#priceId option[selected="selected"]').innerHTML.toUpperCase();
//   console.log(priceID)

//   stripe
//     .createPaymentMethod({
//       type: 'card',
//       card: card,
//       billing_details: {
//         name: billingName,
//       },
//     })
//     .then((result) => {
//       if (result.error) {
//         displayError(result);
//       } else {
//         createSubscription({
//           customerId: customerId,
//           paymentMethodId: result.paymentMethod.id,
//           priceId: priceId,
//         });
//       }
//     });
// }

// function createSubscription({ customerId, paymentMethodId, priceId }) {
//   return (
//     fetch('/dashboard/subscription/', {
//       method: 'post',
//       headers: {
//         'Content-type': 'application/json',
//       },
//       body: JSON.stringify({
//         customerId: customerId,
//         paymentMethodId: paymentMethodId,
//         priceId: priceId,
//       }),
//     })
//       .then((response) => {
//         return response.json();
//       })
//       // If the card is declined, display an error to the user.
//       .then((result) => {
//         if (result.error) {
//           // The card had an error when trying to attach it to a customer.
//           throw result;
//         }
//         return result;
//       })
//       // Normalize the result to contain the object returned by Stripe.
//       // Add the additional details we need.
//       .then((result) => {
//         return {
//           paymentMethodId: paymentMethodId,
//           priceId: priceId,
//           subscription: result,
//         };
//       })
//       // Some payment methods require a customer to be on session
//       // to complete the payment process. Check the status of the
//       // payment intent to handle these actions.
//       .then(handlePaymentThatRequiresCustomerAction)
//       // If attaching this card to a Customer object succeeds,
//       // but attempts to charge the customer fail, you
//       // get a requires_payment_method error.
//       .then(handleRequiresPaymentMethod)
//       // No more actions required. Provision your service for the user.
//       .then(onSubscriptionComplete)
//       .catch((error) => {
//         // An error has happened. Display the failure to the user here.
//         // We utilize the HTML element we created.
//         showCardError(error);
//       })
//   );
// }

// // Confirm Subscription Active



