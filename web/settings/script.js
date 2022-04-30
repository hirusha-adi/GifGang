import $ from "https://cdn.skypack.dev/jquery@3.6.0";

$(() => {
  console.clear()
  // Giving ids
  $('.select').each(function() {
    $(`.select[data-id="${$(this).attr('data-id')}"] .selected`).attr('data-id', $(this).attr('data-id'))
  })
    
  $('input[data-suffix]').each(function(i, obj) {
    
    console.log(obj)
    console.log(i)
    console.log($(this).val())
    
    let suffix = '<div data-for="'+$(this).attr('id')+'" data-suffix="'+($(this).attr('data-suffix'))+'" class="sffxhld"><span class="suffixxx" >'+($(this).attr('data-suffix'))+'</span></div>'
    
    $(this).after(suffix)
    SortSuffix($(this))
  })
})

$('#ucumvA').on('change', function(e) {
  let isChecked = $(this).prop('checked')
  
  if(isChecked === true) {
    $('#ucumvB').prop('disabled', false)
  } else if(isChecked === false) {
    $('#ucumvB').prop('disabled', true)
  }
})


$('input[data-suffix]').on('keyup', function(e)  {
  SortSuffix($(this))
})

$('input[data-suffix]').on('keypress', function(e)  {
  SortSuffix($(this))
})

$('input[data-suffix]').on('keydown', function(e)  {
  SortSuffix($(this))
})

function SortSuffix(dis) {
  if(dis === undefined) {
    dis = $(this)
  }
  
  let suffix = dis.attr('data-suffix')
  let val_length = dis.val().length
  let forId = dis.attr('id')
    
  $('.sffxhld[data-suffix="'+suffix+'"][data-for="'+forId+'"]').css('left', `calc(254px + ((1em / 2) * ${val_length}) + (1px *  ${val_length}))`)
}

$('.selected').on('click', function (e) {
  if(!$(this).attr('data-id')) return console.log(`err: no id`)
  
  $(this).toggleClass('open')
  $(`.select[data-id="${$(this).attr('data-id')}"] .options`).slideToggle(270)
})