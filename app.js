(function(){
  function norm(value){
    return String(value ?? '').trim().toLowerCase().replace(/\s+/g,' ');
  }

  function setResultStyle(result, score, total, unit){
    if(!result) return;
    result.textContent=`Đúng ${score}/${total} ${unit}`;
    result.className='result '+(score===total?'result-perfect':'result-mixed');
  }

  function clearRadioFeedback(form){
    form.querySelectorAll('input[type="radio"]').forEach(input=>{
      const option=input.closest('.option');
      if(!option) return;
      option.classList.remove('answer-correct','answer-wrong');
      if(option.dataset) delete option.dataset.feedback;
    });
  }

  function scoreRadios(formId, answers, resultId){
    const form=document.getElementById(formId); if(!form) return;
    const result=document.getElementById(resultId);
    const btn=form.querySelector('[data-check]');
    const reset=form.querySelector('[data-reset]');

    if(btn) btn.addEventListener('click',()=>{
      clearRadioFeedback(form);
      let score=0;
      Object.entries(answers).forEach(([name,ans])=>{
        const radios=Array.from(form.querySelectorAll(`input[name="${name}"]`));
        const picked=radios.find(r=>r.checked) || null;
        if(!picked) return;
        const option=picked.closest('.option');
        if(picked.value===ans){
          score++;
          if(option){ option.classList.add('answer-correct'); option.dataset.feedback='✓ Đúng'; }
        }else{
          if(option){ option.classList.add('answer-wrong'); option.dataset.feedback='✕ Sai'; }
        }
      });
      setResultStyle(result,score,Object.keys(answers).length,'câu');
    });

    if(reset) reset.addEventListener('click',()=>{
      form.reset();
      clearRadioFeedback(form);
      if(result){ result.textContent=''; result.className='result'; }
    });
  }

  scoreRadios('l1-ex1',{l1q1:'by',l1q2:'on',l1q3:'in',l1q4:'near',l1q5:'in',l1q6:'by',l1q7:'in'},'l1-ex1-result');
  scoreRadios('l2-ex1',{q1:'13th',q2:'Crawford',q3:'0870 292720',q4:'70 Sidney'},'l2-ex1-result');

  // Updated Listening pages. Answers are checked only after the learner presses
  // "Kiểm tra"; the answer key is never injected into the exercise itself.
  scoreRadios('l4-ex1',{q1:'13th',q2:'Crawford',q3:'0870 292720',q4:'70 Sidney'},'l4-ex1-result');
  scoreRadios('l4-ex2',{q1:'Julienne Bailey',q2:'0865701158',q3:'113 Evenlode Road',q4:'3rd April'},'l4-ex2-result');
  scoreRadios('l7-ex1',{q1:'Walliams',q2:'87 Beech Street',q3:'5th April 1984',q4:'0529 865 2411',q5:'shop manager',q6:'12 kilometres',q7:'bus',q8:'cooking, cycling and travel'},'l7-ex1-result');

  const gapForm=document.getElementById('l1-ex2');
  if(gapForm){
    const ans={l1gap8:'reputation',l1gap9:'crime',l1gap10:'conclude',l1gap11:'impact',l1gap12:'influence',l1gap13:'industrial',l1gap14:'surround',l1gap15:'ranks',l1gap16:'reaction',l1gap17:'diverse',l1gap18:'locals',l1gap19:'lifestyle'};
    const r=document.getElementById('l1-ex2-result');
    const clear=()=>gapForm.querySelectorAll('select').forEach(el=>el.classList.remove('answer-correct','answer-wrong'));
    const check=gapForm.querySelector('[data-check]');
    const reset=gapForm.querySelector('[data-reset]');
    if(check) check.addEventListener('click',()=>{
      clear(); let s=0;
      Object.entries(ans).forEach(([n,a])=>{
        const el=gapForm.querySelector(`[name="${n}"]`); if(!el) return;
        if(el.value===a){ s++; el.classList.add('answer-correct'); }
        else if(el.value){ el.classList.add('answer-wrong'); }
      });
      setResultStyle(r,s,Object.keys(ans).length,'ô');
    });
    if(reset) reset.addEventListener('click',()=>{ gapForm.reset(); clear(); if(r){r.textContent='';r.className='result';} });
  }

  function ensureMark(input){
    let mark=input.nextElementSibling;
    if(!mark || !mark.classList.contains('field-feedback')){
      mark=document.createElement('span');
      mark.className='field-feedback';
      input.insertAdjacentElement('afterend',mark);
    }
    return mark;
  }

  function clearTextFeedback(form){
    form.querySelectorAll('[data-answer]').forEach(input=>{
      input.classList.remove('field-correct','field-wrong');
      const mark=input.nextElementSibling;
      if(mark && mark.classList.contains('field-feedback')) mark.remove();
    });
  }

  function scoreTextForm(form){
    const inputs=Array.from(form.querySelectorAll('[data-answer]'));
    const result=form.querySelector('[data-reading-result],[data-text-result]');
    clearTextFeedback(form);
    let score=0;
    inputs.forEach(input=>{
      const accepted=(input.dataset.answer||'').split('|').map(norm).filter(Boolean);
      const value=norm(input.value);
      if(!value) return;
      const ok=accepted.includes(value);
      const mark=ensureMark(input);
      if(ok){
        score++;
        input.classList.add('field-correct');
        mark.textContent='✓ Đúng';
        mark.classList.add('is-correct');
      }else{
        input.classList.add('field-wrong');
        mark.textContent='✕ Sai';
        mark.classList.add('is-wrong');
      }
    });
    setResultStyle(result,score,inputs.length,'câu');
  }

  document.querySelectorAll('form[data-reading-form]').forEach(form=>{
    const check=form.querySelector('[data-check-reading]');
    const reset=form.querySelector('[data-reset-reading]');
    if(check) check.addEventListener('click',()=>scoreTextForm(form));
    if(reset) reset.addEventListener('click',()=>{
      form.reset(); clearTextFeedback(form);
      const result=form.querySelector('[data-reading-result]');
      if(result){result.textContent='';result.className='result';}
    });
  });

  // Text-answer forms can declare accepted variants in data-answer. This is
  // also used for the longer Listening forms and keeps punctuation/spacing
  // tolerant without revealing the key before checking.
  document.querySelectorAll('form[data-text-form]').forEach(form=>{
    const check=form.querySelector('[data-check-text]');
    const reset=form.querySelector('[data-reset-text]');
    if(check) check.addEventListener('click',()=>scoreTextForm(form));
    if(reset) reset.addEventListener('click',()=>{
      form.reset(); clearTextFeedback(form);
      const result=form.querySelector('[data-text-result]');
      if(result){result.textContent='';result.className='result';}
    });
  });

  document.querySelectorAll('details.collapse').forEach(details=>{
    const summary=details.querySelector(':scope > summary');
    if(!summary) return;
    const original=(summary.dataset.label || summary.textContent).replace(/[▼▲]\s*$/,'').trim();
    summary.dataset.label=original;
    const sync=()=>{ summary.textContent=original+(details.open?' ▲':' ▼'); };
    details.addEventListener('toggle',sync); sync();
  });

  const audio=document.getElementById('exercise1-audio'), picker=document.getElementById('audio-file-input'), status=document.getElementById('audio-status');
  if(audio&&picker){
    audio.addEventListener('error',()=>{if(status)status.textContent='Chưa có file MP3 trong bộ web. Bấm “Chọn MP3 Exercise 1” để chọn file bạn đã tải.'});
    picker.addEventListener('change',()=>{const f=picker.files&&picker.files[0];if(!f)return;audio.src=URL.createObjectURL(f);audio.load();if(status)status.textContent='Đã nạp MP3 từ máy của bạn.'});
  }

  document.querySelectorAll('[data-count]').forEach(field=>{
    const targetId=field.dataset.count;
    const target=document.getElementById(targetId);
    const sync=()=>{if(target) target.textContent=`Số từ: ${norm(field.value).split(/\s+/).filter(Boolean).length}`};
    field.addEventListener('input',sync); sync();
  });
})();
