# after https://github.com/terry3041/pyChatGPT 

from pyChatGPT import ChatGPT
import pandas as pd 
import time

from numpy import random

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..bTBe1GBvpwfrZGdj.1cWMi-xhZ6VXC7fPQZPYPcg2sWZ8JryVWiV6oTM-8P486twhoHwYX61uX-dCLCH1jsgbyRD-kivnh4yRRjxQOBwwodfO37TDo7oHOPaVFetM-9nrofLjqI_lz5eTQfG3u8V229O_CK25gpMpmKjsUFUAU1dSdT-AGfG6FN6l5EYm3tU0dNwgZSnwHkoz7lChs3EPTppDPLoMKLFUrWKXHR1eWHaD1CxXHvhboUjA4EUpvB6t6eEf-_sK0if_dbCKiVRL4G1YJbzsxWiu6uOfPI7XGF3V6kDPpM3KwHh7ZGZuQM-rIJIdq0frirR9iCEyIzUpzQ1feeCXeZTrmuKtsjhDNdgMD2JSGSOpNAGI8mw2vpAXSWSMqi0DNPjhQmt3MLazVkaz8VJwacAAefEtQN0zq_jP-goS1MId2lIIFeZRfH1shcNB-3sx25S9AIOfyk8-t-hDyis9cxLHTscd6mm1DX1PcN8MMEb9AcIWyC0ZiMtefQVac6UtxdPQWl3HAUe7mjSpwBsiPc1TgKz6wbZl4weYmGBj8ABGOQmrW634WT6Jp4m10KjcLP1mK9xpab-KCRpq1Ns0nyjc2WLLYz4jInPCY-uiFdvhuP_aIdIqhKMvUgjKZPRPJW0rPcLqDx59qCnziFODg215qIX4Wki3m_WHjogJXpvUBNt0bknnWB4xD8WwRlq0i1qBY9QQdx4U47u7A8Jtdu8jmQceWaBQmVi-9PS-eSYRqu4eDeUucIl9J89NTYS-QRVfYAgSnJP-2zGaIQOuj8pv6L0PeviGInmtovTN38JX1T_wdTb8hQMQGqDn1vCB1drEh9ArqSdXYerpa6z7GY0EVqnwQympBqKlfWoLaA8h-CT8iwk466j89UK-9_IJmX575tGs37b118C31PRrrTCca4_d0AerREzDEGOMpzUlV0kFsLiCP2kzEJ-bOOOd8JDrHsa2E9uTj6BZzzCSXf0p0sx8CWP4_ljsMA3OrtcYo3ZvNRzIH4f3QhYSbbVlRmumcTQg4F4bKRvf8yq5EOE4edMdHEoqAUCkZbe4nlHRS4_vzLVR-5mrYAw3tEGo5g7fDCL7kwWo5gmlhdsEsAurkahMqL4jzVt_kt5fSHdc13cowrOw6pG0XRuezuOt8CJ6mE0vtkIQy12BmaIY1kPInwUyyg2p4oywyQgaqb--ydx_Ep6MZ-u7T6IFC79sH1MGtXLld0GzjW5H4VnEqPrmba8LfH55uD0q_kCEH8PoOnwI6yxCfPqbwAwIjwRsOUdQjCOhIdIMVFSMKZgKvEe-507xCRu3R586sGpj3qAol1lzXf-YezOkukwb6uFuXG76tnkwtjGwtpQC1zOXhCrsdv50GLdyw4MaD-b7znDPWvw_vY-0n3EHHS3NmQYfOII6GoiIRqidCvC1mePJs2r2E6vKr22UZkHR8Gv1LVZugkGg-mlOKN4gD1lDADCnx1IMYiiZG2iUfHnRH9e9bnNEuL8NZKeVemIjaWrJuMe1cSmT9B0hR2hDhssVIXqy0lC9Emvk8nnT8s6Mz9KPQc4VcM-nYYEDfxqXXWR9Nllmz29pkXtEbt3_SRq1RbfiYXd-lSIlcklqeQJlGT6aESHsmQDh7zsxIt4703yheiAFzq7fiU6h2qyp_SiWYC5g7EI1w8znOdMbAb5zO8jUlF-MdzGKexZu_ovcNCkUWdjwSY76Up5v7Gaerl_mkgdx-TNFAJ8x1jwhN9p-jkYOhLLOEyGaYBnq53KvcW3dlUy2cbBzOACQWqHdCxVKs2XyXwKvUqiawstTMUaelUIUzU4WDqvPGGKiKeMhMGmk7X_cQKF5r0D3ANsgm9xX_A5Yo-R4HK8jtrmtFu-Kyvf3BmJbnihOn2je50vePUoX4eao2AIh82YPYVUZ9PaCU5bVkPiHFBRhLF3feup-xPZ3FwlOqQN5xdDkN-GMyS5wX_M79BtPBENlHMHxEiGQFUNX895VhCDiye3P8qd53sUu6rg0WO-WpDNMKhSVVkmvncRPXgra-OwRX1fDbVrMWVwLGsOZgZ90V7ocCvf-Se81E2Z2AkOMj3bG5S0aEKjTakoHFytmQEYTxlPnAzYB8b89MblM99OGTCAzYq8KLHdN04umBbTt6vgFePI2nftHveGIcqN4BBWHL07mtrgcD4Atr1bfoDkgqAU4DKIuoRrweH54ByQkKkErl0HJjGvu3YCJzg1k6iBG8d0wodi2mmYWnsekNcFr-yGzeX1-6U16n8dV70bbQ57bZqIXfQozwpUBNIHi6A7G-EHkU7wmWLTkKTWalV2uWAaQHv5fJb7jlYMokEcER7leUzka_nkIshdFv6mDj-glh0socgia65p6LzdmWYgkrgVZ28EHqiEwrZ19XC9k4vck6IA6XLg93I2ctMavPxUb1zcweTMgqBXF5Hc4aP4pmTf5Bj3_j9AYomANG3loAbmjOHvzTLPJxMQQwShlC9MJ6Uddk8lIn6L8UgzIbEk-h-5bRLRIHk3IeBYCDC6zJZAzo4Hr8EtxAI6u-AoBd-M7CI12gBXCei0p7S58xqTYoabxUKegidgEn3bbjPI0zrv_PrhrWtUEvKt8UimVe6jPv1bS26I0K754PaDTykpwRzQJyI6dUf8k4YafTPIRhqH5cTcLLFlrlw4D1r6SmzxRWq7vgzlZRpPfK7vaC2rvYKA_1RlND4fV9w.-02cBocRommHqhgNLBXw3Q"
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..6JqTJTIGpm3mUXNG.InLG2wGCED-m78MYHJgSIPOIGGQ0GSezGeghmTzeHXTqTH1FZS099r8uNr7UZXFP2384JnKr5kcuLnlYzO06ixPxeLIL_-p3VKTb8SkplL6vEIoorrcFwx-W4s6bbGPaTsb0quJCalG-Ax_8DSQv5_iCHMpyDtXXDYei9Vui75kb9Y1Rf_Aw89HvBeorQHi7ikiI1YMIgZdV79eeZh97rbjeINuak0ua-MQcReXYnkZsU3lKPJ2LmngpX3v0iaq2-5tUJ3kU9-t9yOCkM-1wVzkcOw1OKcRJ0_8ozkUUp4MfImFbSxZMwBvYMivSQYFxX2vgn1BA5p3xmemAWjbQyOdigmpcARFgqfyRXy0Ts6gCnXTJH9WaejBs7n_kUjesDUZgJmT1AbnjkIWT3HaDiIp0-UT3uM27EBVZUWRRuS6ASmjs1DcMqHvCGAPdNijOM0-JBIYU3MkYBZ6LmSSFpbLXh074ACOh6RVLnMwlpHezGgqIC1VNJuEgwTaXYIoiqx98IVc-62D1lE9ELFZJ8f2VaF-R41yASEbJ2Jd9SZUeexW4dSkPCGEEWok49na-jOG-WELCKAuWcvnOdenNKi745jl2agNNeGw9t1H9h0k82qZ_1QzAi5ZqO1AmIi1CqZ3g4n-yL6oDU3Tg56gFpdsxaYex9X1MQK5p3Wmxb8wojdMsRSWEEQ4bJjfiS5YcIlzA7BT2NbdL0bjrZOa8lHsrGty9vPDvDfnniywfEBwO3H-MawhJ7vL19EnHZs8LLSWkrsf9m7NtJ9Q3b9RyiCtDHGuJRndUx7upT3hlufPLAc0qIfyXHGxcJTMsnaexKcTOYHJTcNi-4fRb2hqdefxk1aiQmgS1qpvh_rwepgiAA11O7qqMqqbaguJlESMW6PUflNW9zMbZrOfs4AHfz6T_s8IbI3c-xTl4n0bYAo140yUEOege17YgB41LImqunGJuDT1rfxDaN8c-q7y7eThRKAWkLZoQwks7zkYM4NBnRgCg_YTkW1DIiDl3NKcKz8SyUJCVkbJkAKI6sF6Q9a_1LJGAr4ybA9Dopjq_d95_foAWvDYSKcitKVjI3TQuSrNsxvtGV6WAcjoRt8qOamAtghMF1Aj-64Yxh82DZMRz4VFoSCJ8LiolJc1g1JGM1-JVzQtKDuFMZy3rWl3A8CxCR-PCTEuvyu08qJJtS0JNk9vgXNk2xn0YJVCRNNYgD-S8Dnx-Fzvt9HVV3_dhaJ9eS41X08_IQbqb7_FbO5cHkrRPjUn051Z7sV4yb25j6N5AMfz1UgA02xLX4QX1S4t2dRqYkx3pcmd5-tXH7lZ5q4OGFTWrhtovu40Hcqw039Uyt4ggyqDsDNvfZZeZLxUqJuGtrCvs9wMkbafJk5Ph0rzqAeTIO5y1XPlQMmvHjL_4Sk5eYwzNtc4E9RzpVrY2QPbRpYjCiljC-pMvlfq2CiVt4UebKo1CR8XHoU8n9AIboywaqQTGUwz-fraY_cQ3nq1lXnkZ2yc2vU2n5snLS15K5YlJvBJieZvY5BxDNAFHwKeUgZnGW34Nyy48SYkQK09kGINN_qjmY9o0PL7N36vj-OCUmawYRyPZqeGTE1i6DsSFEPxJ3j0qvZDe4-hvKB7LlbQDGdbW3k6myE-3C2LEY4tb_qj9xAir_iZPLbw0y7L4M7f12EzPDyfoQbzniClz9lVw6ETUwEGX-nJX9J_J2_8UEvmtGNrT2jF514Hhx5_KgQtJYQvvccbJext8KtuVTJ_fk4TJ7GnwZcr5uMgjwd-e8ZK0YxTfpvc_zHzP7egiA_lCM0_cbMbZwejMYiyM-lxpbMApYAhNT6F8VTNJOQhxcGgTrwG94243mh0EMWUYghxKt49mxE2ZgSsLy5ZeksrfacQSfniI2eq-AZ6XG0EnFtMjzQYcRfqgWygbbSIFM5F0OqycCZTizUS-tzZzCCJdT5xXSrT7vHT5CUo4f4E_WdCLPeQyneowA_6MxiyNXGd_yWpohDkvjlKDQCSpOhACNVDXnO1hzKxSY7kF7kC3G4TOOJCbQiOavCNoJtD2xcTAkwaPtrNZOjm73SqjBG001rwQpNGT1P5MLuryOn6UlQfBKnkgqwuDaLkm1HUS6H-cw5mM-boskpH9ezMV_dOv_1IHka5B-u0I8C7AyNxAk-PCR-aPfXD-lKxWQvJxrrmNqGEQ9Z7zB2kZqQZCW2KSYbrNWsk-aYf6UNbNlY0d-OFWefQZmAqR5222rOSR-rGa7WMVtwb6yJG8FYG7qdrurIqsXVcJ8vWuYKmEZsK5SZ6tbqjrv4TDVaOEQtih5-0v1fn2j9EXb0Nx0A-kDqKai9Rug0iEzA98OU6JVH9jnhWqt1ar5k8B2YrqvpIbmQr1eo4Xpy5oH0i0vbbfcLcn9xgL7Vrf8LBdNjStDC8TyGPg_i-XL7ShFC3vQj6kOHS_TImeYo7aka4JQXogF3I1chxeh36QiorULzFNdzVEb-PsA5fgeFfndf3NSuT0hG0Q9fgmR5eX-iY7X-zD1jt6M59q9LRhfo7cMO3_DwTP2DhFfeS8zRdkNS1xcEwsXVhZm7hOCdzz42AJxtbYQ2nWh_FennMXEiSucHnMWyL4ngWlRuSRSoNyMyOFmxOvHjJEP4MBec63k_Ti5eDF8JU2FBkdF2eY2cdlhfCShz6zvILv9Pwtaly0xqn8UxkDDJeWGcqqoRAI9wxORkjbYhMX._nYJzk19w7JO_BAUTCN0lA"
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..THGIrHvck2DNv1OV.jK1dcKmdA0D8o1GdaCSgyCdnmHuXnJZD8As2yWqjuHYEkEspMroKUtkNW7N_d5FW4SAGgU2AF0ottJsa-rkq0RAWcPFcKVqz3rVVvHQl-9yAnm2qK5GzBiFNFNjeAIUz9ru-FPh9ae02wX5m34_m3TKDEDU_iGC6PQZDSJgjQZwAiKBvwJ27-Ws94RVmf8QARj415x3d5eBvt_ZFRxNWzalscbicAif5iLTFQZZv5JDyCbX2oz8lCP6JbqflZnIk24_PyvmY4aE0yQxWq6LMaS25SEAp8yQDoTrYsRNTlxoUFdueK4N-WO1vkDv7jD8TPKaWq1lfAtWNU8-CLk7ikvNlrPVkfpuIvl1osrOxVeNyuMfTJcHGx9yPNvyqm7DZkZWkBjiZhsiATj98pfqeJo0RSiqjb2TNWQsbA2VRNOHlTXwW6jKOG4KeN5UwG6IvTiXZ8STKc2qlJnRlaxpac7WSDXuL1srNvZ4g-M5T6uwk-dtv2-6TLHfkwbBkHzadMpNBcYPnRJINn9rWG8UEjZMJeu4rRQXnXvTBlIpVNKyQIq_ZMEVQZSK3bwHvumuEn07W2PagDTu8oi5QEFpa2vBz-hRrHPVM4GG1s0B9Qm21sll1LnMkOOVNUN56Bti5-BgZwxk61-kkYeDtsDlkbs-cj01LUESC-QRfGxhgpJGxRMLVK5hYgBO44yHgdDOfvCQeE5sHQPeqJ6QYuzrT8YPUfHXIFlsheR7ROyDstQ_zUFQQAtY_pEh41X63aoobi19Z2i8NU-fglHFdQ15PgLA_AHWjyVWhCB6iOdT2Lw_lGU79uDJEAFAha-dW3R99Jcs5hqrdx7Idoudq1tiRs-qsPr4LRMYGXKG89ygb2pmRiovCzAHSYj7SJuWw3pne7WG_fjRtpZBWjtX5h1uxaHe-LxRk1uOSYCUHwS1icthy-KWURni5MTyF7OUALKFQ8UNlDCtDF5_RyKRk2ivvasDwV4439Gv2GOV9cvdxr8Cz-d1g4BeIiu7LEBLJFxE3dlSyqX6x0NxD3RSyaUYnjsE8zMzZgdH1juvw_Wa8-tku6vWeejFdLNOy_bUXM3QQmO7rR1o9PNdQ8jJLArKAU1x8AZhtK98v3quul9hhVr0BTgt3VF3RQKtGawwoku85VKpOCsJjDdJFSyNokQCKDlWfGM6ZHKZRU6opA6lgwjx2AQHLcPCoVfsy8VNnSgC1SbHmVLCgIzCPak1EWs_9iJWx1-oJ-BpcJ6Zjho78xj_E10kMdfYgvtMPbynPfucMdKE1d4dly0KiRC33HTqykalicTqjY2XI3BfpEnomG9HcLeh0PrBR_M7lQmqvBvaWmVlVhWfpQVoAmlJNOcB6sNHZTw0y13_q3y5Wtbw15y2J0_JqJpKUr42g_IeH5xgH0f6ni8eMkvElC7jHqx6AFaBEFD-OYYw7SJwmyICHg0Y4r8BdM97JhmLmgPDE6O6rdiwmjuS0VYKayBLBCsB6SE9S6NqnEycfXML-PjeeP9dyV-QhmHvYwOg-fx54HWP4QOxNOQ22bJRCJQBlIlpOZWyyiXomiyYzUVRqzIzpsxiszv4NmC6pSAw-OhsSjdCAsHCDubMJcEMFuKcZQyNnBIjNtb5GGdm4qDFs3bQRcuJeuK0fzOst0gCRAueq_VRvR6qsxwgPPZ5xxFuSUhKj3mH75mHh2_uVabPHGhR8NAfDqkw9RLMD7a--UumhY67v_MAyLS88pcpPc9W2silYkeAogncurs53ioVuKamz6M8XbrWcK3JvoV_G4ljDkOSbtmBzfiTG84ul7jYzik5s-cFKNtm8ZOKU5p7FNitbV03lWzhlj16EcbI1PFFa5VkfnIqnPoAoih5ZTqngaEsY2uikY6yNoAiw4-ZretpepX1C1VDCDvn2QcOCZIQhoNBBM-qySj4IMiioowpR6Pfl1-QnckH6okilDm94hMywRE6ZOFjuonbkL5frLg1s1juKFqiZ89RkeqT3RwUyoppSmBf0_vYxWFJLKnkI4AhHdpGdhhbJvXbPDamOCGzyJhwam81mtOaULd5thdsjGL3yLkUbloiPh9mfnKdaCqp9nZMIzDJ6pCDJ2r_efeATBQEVczkgMoiNS6yBcEV-u4vVTWoe5yS6ryh3ULbD5DEgB3t9JvPG0U0Tc96GH6Z-3r6z3Adl7XN69wZbQZiupqMgAXb6Oro7QzhYoubypVn3CrLF8AenwpkCrwHbZQPrJ87maAZtomg_H_poi9fMPqnI3h9TcwQI0BbZHOuqRjZIk8lqOZUovkIA8noXnu4SjiP3UGfBQKOtiuKCfCmVJqFL1DdULmPN5lw9hOFj6_qfuX3S4VbjAdO6GPKJwftGWEYnMyDm3K87LQ8yK_oakj6GeYwnv31glq81T0pHwICGFlKLOkw7Le4l8JVdxXm7SPnNwcECpmt1QMtnmL8HKKhXWz9n_R7ulpB5RzlIQYwN6nwJN05F_KGW0OQ2XIcUmssW3Ev9qw_LMeQkPXEtylFAjztWNFEWNSFYiQcQrCpFJMbAmfYCb-ZPzggauZxVBPYavqvQHKp7HH-h3BblwJ47cLiJgspUIX7aqwc7Y5XbtPH55jjrEnphpaG4AS8rS1C4Y68qAhi81i2G-c87iBS_FMAH2PPqaGvhxUWTcRBJ3UOKYxlSV9ixZQ.u6u1nW9ySo-3IdthQQUlxQ"

#"eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0" # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)# conversation_id="d9debae4-854a-43e4-8b92-4e593795c820")  # auth with session token

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why was the math book sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the cookie go to the doctor? Because it was feeling crumbly.",
    "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
    "Why did the frog call his insurance company? He had a jump in his car.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the hipster burn his tongue? He drank his coffee before it was cool.",
    "Why don't oysters give to charity? Because they're shellfish.",
    "Why did the computer go to the doctor? Because it had a virus.",
    "Why did the banana go to the doctor? Because it wasn't peeling well.",
    "Why did the coffee file a police report? Because it got mugged.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the man put his money in the freezer? He wanted cold hard cash.",
    "Why don't seagulls fly over the bay? Because then they'd be bagels.",
    "Why did the chicken go to the seance? To talk to the other side.",
    "Why was the belt sent to jail? Because it held up a pair of pants.",
    "Why did the chicken cross the road? To get to the other side.",
    "Why did the computer go to the doctor? Because it had a byte.",
    "Why did the cow go to outer space? To see the moooon.",
    "Why did the man put his money in the blender? He wanted to make liquid assets.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call an alligator in a vest? An investigator.",
]

jokes_ =  [
    'Why did the cookie go to the gym? To get a little crumbly.',
    'Why did the cookie go to the gym? To get a-cookie-dized.',
    'Why did the chicken go to the seance? To talk to the other side.',
    'Why did the chicken wear a tuxedo? Because it was a formal occasion.',
    "Why did the banana go out with the prune? Because it couldn't get a date.",
    'Why did the banana split? Because it saw the ice cream.',
    'Why did the bicycle stand up by itself? Because it was two tired.',
    'Why did the birdie go to the seance? To get in touch with its other side.',
    'Why did the chicken go to the party? To dance the fowl.',
    'Why did the computer cold? Because it left its Windows open.',
    'Why did the computer go to the doctor? It had a byte.',
    'Why did the cookie go to the meeting? Because it was a shortbread.',
    'Why did the duck cross the playground? To get to the other slide.',
    'Why did the duck cross the road? To get to the other pond.',
    'Why did the duck go to the doctor? Because it had a bill in its throat.',
    'Why did the man put his money in the blender? He wanted to make time fly.',
    'Why did the man put his money in the oven? He wanted warm dough.',
    'Why did the man put his watch in the blender? He wanted to make time fly.',
    'Why did the squirrel cross the road? To get to the nut store.',
    'Why was the physics book sad? Because it had so many formulas to memorize and so few friends to share them with.',
    "Why don't bicycles fall over? Because they're two-tired.",
    'Why did the skeleton go to the party? To get a little bit more "body" into his social life.', ]

prompts = [F"Can you explain why this joke is funny: \n{j}" for j in jokes]

#bot = ChatGPT()
#n = 1100 # number of generated jokes 
path = 'joke_explanation_3'
try:
    df = pd.read_pickle(path)
except:
    # create dataframe and 
    df = pd.DataFrame({"prompt": [], "response": []})
    df.to_pickle(path)
print(df.shape)
#print(prompts)
#print('####', df.shape[1])

# i = df.shape%len(prompts)
j = 0 # max prompt per hour 
n = 100
i = 0
for elem in prompts: ############################################################################
    print(i, n-df.shape[0])
    
    if j > 74:
        print("Reached max. Sleep for one hour.")
        time.sleep(900)
        print("15 minutes passed.")
        time.sleep(900)
        print("Half an hour left")
        time.sleep(900)
        print("15 more minutes.")
        time.sleep(900)
        j = 1
    print('new loop')
    df = pd.read_pickle(path)
    #prompt_number = df.shape[0]%len(prompts)
    #print(prompt_number)
    prompt = elem # F'What kind of sentence is that: {elem}'
    if prompt in df.prompt.tolist():
        i+=1 
        print('prompt already in df')
    else:
        j += 1
        try:
            api.refresh_chat_page()
            resp = api.send_message(prompt) 
            time.sleep(3)
            print(F"{i}: {prompt} - {resp}")
            
            # print(i ==df.shape[1]+1) # this does not work whith multiple iterations        
            data = {"prompt": [prompt], "response": [resp]}
            df2 = pd.DataFrame(data)
            df = pd.concat([df,df2])
            df.to_pickle(path) 
            time.sleep(3)
            i+=1
        except TimeoutException as ex:
            print(F"Oops! {ex}")
            api.refresh_chat_page()
            time.sleep(3)
        except ValueError as err:
            print(F"Oops! {err}")
            print(type(err))
            if "Too many requests" in str(err): 
                print(err)#)"I'll try again in 15 Minutes")
                #time.sleep(900)
                #api.refresh_chat_page()
                #raise
            if "Only one message at a time":
                i=i-1
                #raise
            else: 
                print(F'something else: {err}')

print("### reached the end ###")

