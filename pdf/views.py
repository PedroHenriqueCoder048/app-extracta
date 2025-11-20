import pytesseract
from pdf2image import convert_from_bytes
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama.llms import OllamaLLM
from django.shortcuts import render
import json
from django.conf import settings


def home(request):
    context = {}
    if request.method == 'POST':
        file_pdf = request.FILES.get('formFile')
        format_data = request.POST.get("formatData")
        context['method']=request.method
        if not file_pdf:
            context['file']=file_pdf
            return render(request,'index.html',context,status=200)
        
        pytesseract.pytesseract.tesseract_cmd  = settings.TESSERACT_PATH
        pdf_bytes = file_pdf.read()
        pages = convert_from_bytes(
            pdf_bytes,
            poppler_path=settings.POPPLE_PATH
        )
        text_data = ''
        for page in pages:
            text_data += pytesseract.image_to_string(page) + '\n'

        print(text_data)
        llm = OllamaLLM(
            model='deepseek-r1:7b',
            temperature=0,
            base_url="http://host.docker.internal:11434",
        )

        if format_data == 'HTML':
            
            prompt = PromptTemplate(
                input_variables=["texto"],
                template="""
                Extraia os dados do texto abaixo.
                Responda APENAS em HTML, sem explicações.

                Texto:
                {texto}
            """
            )

            chain = prompt | llm 

            response_data = chain.invoke({'texto':text_data})


            context['response'] = response_data
            context['file']=file_pdf
            return render(request,'index.html',context,status=200)
        
        elif format_data == 'JSON':
            
            parser = JsonOutputParser()
            prompt = PromptTemplate(
                input_variables=["texto"],
                partial_variables={"format_instructions": parser.get_format_instructions()},
                template="""
                Extraia os dados do texto abaixo.

                Responda APENAS com um JSON válido em snake_case, sem explicações
                Siga exatamente estas instruções de formato:

                {format_instructions}
                
                Texto:
                {texto}
            """
            )

            chain = prompt | llm | parser

            response_data = chain.invoke({'texto':text_data})

            context['response'] = json.dumps(response_data,ensure_ascii=False)
            context['file']=file_pdf
            return render(request,'index.html',context,status=200)

        elif format_data == 'SQL':
            
            prompt = PromptTemplate(
                input_variables=["texto"],
                template="""
                Extraia os dados do texto abaixo.
                Se identificar estrutura como tabelas,vetores ou matrizes de dados que estão relacionados, crie um script em sql simples, sem explicações.
                Os textos que não de dados relacionais ou que não fazem sentido ignore.
                Faça os scripts de criar, editar e deletar.

                Texto:
                {texto}
            """
            )

            chain = prompt | llm 

            response_data = chain.invoke({'texto':text_data})

            context['response'] = response_data
            context['file']=file_pdf
            return render(request,'index.html',context,status=200)

        else:
            
            prompt = PromptTemplate(
                input_variables=["texto"],
                template="""
                Extraia os dados do texto abaixo.
                Retorne um texto ajustado e apenas com as partes importantes, sem explicações.
                Evite usar * .
                
                Texto:
                {texto}
            """
            )

            chain = prompt | llm 

            response_data = chain.invoke({'texto':text_data})


            context['response'] = response_data
            context['file']=file_pdf
            return render(request,'index.html',context,status=200)

    context['method']=request.method
    return render(request,'index.html',context,status=200)
