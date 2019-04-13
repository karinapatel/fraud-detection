// Load console updates when doc is ready and when the dashboard button is clicked
$(document).ready(function(){
    console.log('Document is ready')

$('#see-dashboard').click(async function(){
    console.log('See dashboard button was clicked')
    
    const names = await $.ajax('/table')

    const data = {
        names,
    } 

    console.log(data)

    const response = await $.ajax('/table')
    console.log(response)
})
    })

