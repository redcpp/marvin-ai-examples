from marvin import Bot

class ResumeAnalyzer:
    def __init__(self):
        self.bot = Bot(
            name="ResumeAnalyzer",
            instructions=("Analyze a set of resumes for a specific job position, "
                          "assign a score for each resume.")
        )

    async def analyze_resumes(self, job_position, resumes):
        scores = []
        for resume in resumes:
            name = await self.bot.say(f"Get the name of the candidate for resume {resume} without any other prose")
            result = await self.bot.say(f"Assign a score to the resume {resume} for the job position '{job_position}'")
            score = await self.bot.say(f"Extract only the score of the candidate for {result.content} without any other prose")
            scores.append({
                "name": name.content,
                "score": score.content,
                "analysis": result.content
            })
        return scores
