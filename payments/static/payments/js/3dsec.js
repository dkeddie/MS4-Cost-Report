function _3dsec(stripe_public_key, pi_secret) {
  document.addEventListener("DOMContentLoaded", function(event){
    var stripe = Stripe(stripe_public_key);

    stripe.confirmCardPayment(pi_secret).then(function(result){
      if (result.error) {
        $("#3ds_result").text("Error!");
        $("#3ds_result").addClass("text-danger");
      } else {
        $("#3ds_result").removeClass("d-none");
        setTimeout(() => {
          window.location = url
        }, 5000);
      }
    })
  })
}