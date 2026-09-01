(function(){
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
        const correct=radios.find(r=>r.value===ans) || null;

        if(picked && picked.value===ans){
          score++;
          const option=picked.closest('.option');
          if(option){
            option.classList.add('answer-correct');
            if(option.dataset) option.dataset.feedback='✓ Đúng';
          }
        }else{
          if(picked){
            const pickedOption=picked.closest('.option');
            if(pickedOption){
              pickedOption.classList.add('answer-wrong');
              if(pickedOption.dataset) pickedOption.dataset.feedback='✕ Sai';
            }
          }
          if(correct){
            const correctOption=correct.closest('.option');
            if(correctOption){
              correctOption.classList.add('answer-correct');
              if(correctOption.dataset) correctOption.dataset.feedback='✓ Đáp án đúng';
            }
          }
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

  const gapForm=document.getElementById('l1-ex2');
  if(gapForm){
    const ans={l1gap8:'reputation',l1gap9:'crime',l1gap10:'conclude',l1gap11:'impact',l1gap12:'influence',l1gap13:'industrial',l1gap14:'surround',l1gap15:'ranks',l1gap16:'reaction',l1gap17:'diverse',l1gap18:'locals',l1gap19:'lifestyle'};
    const r=document.getElementById('l1-ex2-result');
    const clearGapFeedback=()=>{
      gapForm.querySelectorAll('select').forEach(el=>{
        el.classList.remove('answer-correct','answer-wrong');
        if(el.dataset) delete el.dataset.correctAnswer;
        if('title' in el) el.title='';
      });
    };

    gapForm.querySelector('[data-check]').addEventListener('click',()=>{
      clearGapFeedback();
      let s=0;
      Object.entries(ans).forEach(([n,a])=>{
        const el=gapForm.querySelector(`[name="${n}"]`);
        if(!el) return;
        if(el.value===a){
          s++;
          el.classList.add('answer-correct');
        }else{
          el.classList.add('answer-wrong');
          if(el.dataset) el.dataset.correctAnswer=a;
          if('title' in el) el.title=`Đáp án đúng: ${a}`;
        }
      });
      setResultStyle(r,s,Object.keys(ans).length,'ô');
    });

    gapForm.querySelector('[data-reset]').addEventListener('click',()=>{
      gapForm.reset();
      clearGapFeedback();
      if(r){ r.textContent=''; r.className='result'; }
    });
  }

  const audio=document.getElementById('exercise1-audio'), picker=document.getElementById('audio-file-input'), status=document.getElementById('audio-status');
  if(audio&&picker){
    audio.addEventListener('error',()=>{if(status)status.textContent='Chưa có file MP3 trong bộ web. Bấm “Chọn MP3 Exercise 1” để chọn file bạn đã tải.'});
    picker.addEventListener('change',()=>{const f=picker.files&&picker.files[0];if(!f)return;audio.src=URL.createObjectURL(f);audio.load();if(status)status.textContent='Đã nạp MP3 từ máy của bạn.'});
  }
})();
