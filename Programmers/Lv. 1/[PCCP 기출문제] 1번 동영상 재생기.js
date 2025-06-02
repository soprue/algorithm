function timeToSeconds(timeStr) {
    const [min, sec] = timeStr.split(":").map(Number);
    return min * 60 + sec;
}

function isInOp(pos, start, end) {
    return start <= pos && pos <= end
}

function solution(video_len, pos, op_start, op_end, commands) {
    pos = timeToSeconds(pos);
    const videoSeconds = timeToSeconds(video_len);
    const opStartSec = timeToSeconds(op_start);
    const opEndSec = timeToSeconds(op_end);
    
    if(isInOp(pos, opStartSec, opEndSec)) pos = opEndSec;
    
    for (const command of commands) {
        pos += command === "next" ? 10 : -10;
        pos = Math.max(0, Math.min(pos, videoSeconds));

        if(isInOp(pos, opStartSec, opEndSec)) pos = opEndSec;
    }
    
    const min = String(Math.floor(pos / 60)).padStart(2, "0");
    const sec = String(pos % 60).padStart(2, "0");
    return `${min}:${sec}`;
}
