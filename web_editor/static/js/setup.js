let sequences = [];

let cubeArray = [[''], [''], [''], [''], [''], 0.8];

$(document).ready(() => {
    prepareData();
    let content = '';
    for (let level = 0; level < 5; level++){
        content += '<div class="level l' + level + '">';
        for (let square = 0; square < 25; square++) {
            content += '<div class="square off s' + square + '"></div>';
        }
        content += '</div>';
    }
    $('body').append(content);

    let iter = 0;
    $('.level').each(function() {
        $(this).css('transform', 'translateY(' + (155 * iter++) + 'px)' + $('.level').css('transform'));
    });
}).on('click', '.on', function() {
    if (!$(this).hasClass('reserved')) {
        $(this).removeClass('on');
        $(this).addClass('off');
        extractData($(this), false);
    }
}).on('click', '.off', function() {
    if (!$(this).hasClass('reserved')) {
        $(this).removeClass('off');
        $(this).addClass('on');
        extractData($(this), true);
    }
}).on('paste', 'textarea', function() {
    setTimeout(() => {
        let paste = $(this).val()
            .replaceAll('[', '')
            .replaceAll(']', '')
            .replaceAll('.', '')
            .replaceAll(',', '')
            .replaceAll('"', '')
            .replaceAll(' ', '')
            .replaceAll(':', '')
            .replaceAll('{', '')
            .replaceAll('}', '')
            .replaceAll('\n', '');

        for (let i = 0; i < paste.length; i++) {
            if (paste[i] != '0' && paste[i] != '1') {
                paste = paste.replaceAt(i, '0');
            }
        }

        if (paste.length < 125) {
            paste = paste + '0'.repeat(125 - paste.length);
        }
        paste = paste.substring(0, 125);
        cubeArray[0] = paste.substring(0, 25);
        cubeArray[1] = paste.substring(25, 50);
        cubeArray[2] = paste.substring(50, 75);
        cubeArray[3] = paste.substring(75, 100);
        cubeArray[4] = paste.substring(100, 125);
        commitData();
        showData();
    })
}).on('keyup', 'textarea', function() {
    setTimeout(() => {
        commitData();
    }, 0);
}).on('click', '.add-sequence', function() {
    cubeArray[5] = $('.sequence-delay').val();
    sequences.push(cubeArray.slice(0));
    let nr = sequences.length;
    $('.select-sequence').append('<option value="' + nr + '">' + nr + '</option>');
    $('.select-sequence').val(nr).change();
}).on('click', '.delete-sequence', function() {
    let val = $('.select-sequence').val();
    if (val != 0) {
        $('.select-sequence option:selected').remove();
        sequences.splice(val - 1, 1);
        newSelectOption($('.select-sequence'))
    }
    prepareData();
    showData();
}).on('change', '.select-sequence', function() {
    let nr = $('.select-sequence option:selected').val() - 1;
    if (nr >= 0) {
        cubeArray = sequences[nr].slice(0);
        commitData();
        showData();
    } else {
        prepareData();
        showData();
    }
}).on('click', '.run-sequence', async function() {
    $('button').attr('disabled', true);
    $('textarea').attr('disabled', true);
    $('select').attr('disabled', true);
    $('input').attr('disabled', true);
    $('.square').addClass('reserved')

    for (let i = 0; i < sequences.length; i++) {
        cubeArray = sequences[i].slice(0);
        commitData();
        showData();
        await sleep(cubeArray[5] * 1000);
    }

    $('button').attr('disabled', false);
    $('textarea').attr('disabled', false);
    $('select').attr('disabled', false);
    $('input').attr('disabled', false);
    $('.square').removeClass('reserved')
}).on('click', '.download-sequence', function() {
    download();
});

function prepareData() {
    cubeArray.forEach((element, index) => {
        cubeArray[index] = "0000000000000000000000000";
    });
    cubeArray[5] = 0.1;
    commitData();
}

function extractData($object, isOn) {
    level = parseInt($object.closest('.level').attr('class').replace('level', '').replace(/\s/g, '').replace('l', ''));
    charNr = parseInt($object.attr('class').replace('square', '').replace('off', '').replace(/\s/g, '').replace('s', ''));
    cubeArray[level] = cubeArray[level].replaceAt(charNr, parseInt(+isOn).toString());
    commitData();
    displayDataOnServer();
}

function commitData() {
    $('textarea').val(cubeArray[0] + '\n' + cubeArray[1] + '\n' + cubeArray[2] + '\n' + cubeArray[3] + '\n' + cubeArray[4]);
    $('.sequence-delay').val(cubeArray[5])
}

function showData() {
    cubeArray.forEach((element, index) => {
        for (let i = 0; i < element.length; i++) {
            if (element.at(i) == '1') {
                $('.l' + index + ' .s' + i).addClass('on');
                $('.l' + index + ' .s' + i).removeClass('off');
            } else {
                $('.l' + index + ' .s' + i).addClass('off');
                $('.l' + index + ' .s' + i).removeClass('on');
            }
        }
    });
    displayDataOnServer();
}

function newSelectOption($select) {
    $select.html('<option selected value="0">New Sequence</option>');
    for (let i = 0; i < sequences.length; i++) {
        $select.append('<option value="' + (i + 1) + '">' + (i + 1) + '</option>')
    }
}

function download() {
    if (!sequences.length) return false;

    let $element = $('<a>');
    let text = JSON.stringify(sequences);
    let filename = $('.file-name').val();
    if (filename == '') filename = 'sequence';
    filename = filename + '.json';

    $element.attr('href', 'data:application/json,' + encodeURIComponent(text));
    $element.attr('download', filename);
    $element.hide();
    
    $('body').append($element);
    $element[0].click();
    $('body').remove($element);
}

function displayDataOnServer() {
    $.ajax({
        url: '/data/',
        type: 'POST',
        data: JSON.stringify(cubeArray),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
    });
}

String.prototype.replaceAt = function(index, replacement) {
    return this.substring(0, index) + replacement + this.substring(index + replacement.length);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}