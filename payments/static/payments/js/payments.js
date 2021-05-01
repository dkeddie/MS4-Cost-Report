
// 'PAYMENT METHOD' PAGE

// Automatic select of first option as default
$(window).ready(function () {
  $('#option1').focus()
})

// Updates selected subscription frequency in hidden input
$('.btn-wide').click(function () {
  var x = $(this).children().val()
  $('#priceId').val(x)
})


// 'CARD' and 'THANK YOU' PAGE

// Display Plan Details
var plan_name = ""
var plan_id = $('input[name="stripe_plan_id"]').val()

if (plan_id === "price_1IakCVLti2F8BZ1vMCS0D56C") {
  console.log("yes")
  plan_name = "Daily @ £1 per day"
} else if (plan_id === "price_1IakBnLti2F8BZ1vmf00rG9b") {
  plan_name = "Monthly @ £10 per month"
} else {
  plan_name = "Yearly @ £100 per year"
}

$('input[name="subscription"]').val(plan_name)


